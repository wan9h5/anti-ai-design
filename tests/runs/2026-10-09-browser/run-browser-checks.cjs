// Run with node. Resolve dependencies through NODE_PATH; set CHROMIUM_EXECUTABLE.
// Optional EVIDENCE_LABEL preserves each run. Synthetic local files only.
const {chromium}=require('playwright');
const AxeBuilder=require('@axe-core/playwright').default;
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const assert=require('assert/strict');
const base=__dirname,label=process.env.EVIDENCE_LABEL||'final';
const ids=['create-triage','dense-expert','expressive-brand','truthful-demo','stale-result','chart-equivalent','form-recovery'];
const checks=[],audits=[],errors=[],requests=[];
async function check(id,name,fn){try{await fn();checks.push({id,name,result:'pass'})}catch(e){checks.push({id,name,result:'fail',error:e.message})}}
async function text(p,s,re){assert.match(await p.locator(s).innerText(),re)}
async function focused(p,s){assert.equal(await p.locator(s).evaluate(e=>e===document.activeElement),true)}
async function keyboardTo(p,s){for(let i=0;i<40;i++){await p.keyboard.press('Tab');if(await p.locator(s).evaluate(e=>e===document.activeElement))return;}throw Error('Not reached by Tab: '+s)}
async function audit(p,id,state){let r=await new AxeBuilder({page:p}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();audits.push({id,state,violations:r.violations,incomplete:r.incomplete,passes:r.passes.map(x=>x.id)});await check(id,'axe '+state,()=>assert.equal(r.violations.length,0,r.violations.map(x=>x.id).join(',')))}
async function main(){
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_EXECUTABLE,headless:true});
for(const id of ids){const context=await browser.newContext({viewport:{width:1280,height:900}}),p=await context.newPage();p.on('pageerror',e=>errors.push({id,error:e.message}));p.on('request',r=>{if(!r.url().startsWith('file:'))requests.push({id,url:r.url()})});
const open=()=>p.goto(pathToFileURL(path.join(base,id+'.html')).href);
await open();await audit(p,id,'initial');
if(id==='chart-equivalent')await check(id,'SVG axes and grid do not create filled polygons',async()=>assert.ok(await p.locator('.axis,.grid').evaluateAll(es=>es.every(e=>getComputedStyle(e).fill==='none'))));
if(id==='expressive-brand'||id==='chart-equivalent')await check(id,'manual-source contrast for axe incomplete',async()=>{
 const colors=await p.evaluate(id=>id==='expressive-brand'?{fg:getComputedStyle(document.querySelector('.intro')).color,bg:['#ffe4a8','#f7b68b','#ed9a88']}:{fg:getComputedStyle(document.querySelector('svg text')).fill,bg:['#ffffff']},id);
 function lum(s){let ns=s.startsWith('#')?[1,3,5].map(i=>parseInt(s.slice(i,i+2),16)):s.match(/[\d.]+/g).slice(0,3).map(Number);return ns.map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4}).reduce((s,x,i)=>s+x*[.2126,.7152,.0722][i],0)}
 const ratios=colors.bg.map(bg=>{let a=lum(colors.fg),b=lum(bg);return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)});assert.ok(Math.min(...ratios)>=4.5,JSON.stringify({colors,ratios}));checks.push({id,name:'measured contrast evidence',result:'pass',colors,ratios});
});
await check(id,'primary keyboard path',async()=>{
 if(id==='create-triage'){await keyboardTo(p,'#severity');await p.keyboard.press('ArrowDown');await p.keyboard.press('Tab');await focused(p,'#owner');await p.locator('#severity').selectOption('all');await p.locator('#owner').selectOption('unowned');await keyboardTo(p,'[data-action="claim"]');await p.keyboard.press('Enter');await text(p,'#status',/claimed locally/);await focused(p,'#owner');await keyboardTo(p,'#empty-clear');await p.keyboard.press('Enter');await focused(p,'#clear');await keyboardTo(p,'[data-action="release"]');await p.keyboard.press('Space');await text(p,'#status',/released locally/)}
 if(id==='dense-expert'){await keyboardTo(p,'#resolve');await p.keyboard.press('Enter');await text(p,'#ac01-status',/Resolved/);await p.keyboard.press('Space');await text(p,'#ac01-status',/Review/);await keyboardTo(p,'#inspect');await p.keyboard.press('Enter');await focused(p,'#close-invoice');await p.keyboard.press('Escape');await focused(p,'#inspect');assert.equal(await p.locator('#invoice').isVisible(),false)}
 if(id==='expressive-brand'){await keyboardTo(p,'a[href="#register"]');await p.keyboard.press('Enter');await keyboardTo(p,'#name');await p.keyboard.type('Alex');await p.keyboard.press('Tab');await focused(p,'#email');await p.keyboard.type('bad');await p.keyboard.press('Enter');await focused(p,'#email');await text(p,'#email-error',/email address/);await p.locator('#email').fill('alex@example.com');await p.keyboard.press('Enter');await focused(p,'#summary-title');await text(p,'#result-status',/No reservation/);await audit(p,id,'preview');await keyboardTo(p,'#edit');await p.keyboard.press('Enter');await focused(p,'#name');assert.equal(await p.locator('#name').inputValue(),'Alex')}
 if(id==='truthful-demo'){await keyboardTo(p,'#sample');await p.keyboard.press('ArrowDown');await p.keyboard.press('Tab');await focused(p,'#analyze');await p.keyboard.press('Enter');await text(p,'#mean',/^3$/);await text(p,'#range',/^0$/);await text(p,'#status',/not run/);await p.locator('#sample').selectOption('SYN-01');assert.equal(await p.locator('#output').isVisible(),false);await p.locator('#analyze').click();await text(p,'#mean',/^4$/);await audit(p,id,'result')}
 if(id==='stale-result'){await keyboardTo(p,'#threshold');await p.locator('#threshold').fill('15');await text(p,'#status',/Previous result/);await text(p,'#result',/2 of 3/);await p.keyboard.press('Enter');await text(p,'#result',/1 of 3.*15/);assert.equal(await p.locator('#history-body tr').count(),2);await p.locator('#threshold').fill('');await p.keyboard.press('Enter');await focused(p,'#threshold');assert.equal(await p.locator('#input-error').isVisible(),true);await p.locator('#threshold').fill('20');await p.keyboard.press('Enter');await text(p,'#result',/0 of 3/);await audit(p,id,'history')}
 if(id==='chart-equivalent'){await keyboardTo(p,'.chart-scroll');assert.deepEqual(await p.locator('tbody td').allTextContents(),['18','25','21','30','24','16']);await text(p,'figcaption',/no hovering/i)}
 if(id==='form-recovery'){await keyboardTo(p,'#name');await p.keyboard.type('Alex');await p.keyboard.press('Tab');await p.keyboard.type('bad');await p.keyboard.press('Enter');await focused(p,'#email');assert.equal(await p.locator('#name').inputValue(),'Alex');await p.locator('#email').fill('alex@example.com');await p.locator('#service').selectOption('Outage');await p.locator('#submit').click();await text(p,'#status',/outage/);await audit(p,id,'outage');await p.locator('#service').selectOption('Available');await p.locator('#submit').click();await text(p,'#status',/No data was sent/);assert.equal(await p.locator('#email').inputValue(),'alex@example.com')}
});
await open();await keyboardTo(p,id==='chart-equivalent'?'.chart-scroll':id==='dense-expert'?'.table-region':id==='create-triage'?'#severity':id==='truthful-demo'?'#sample':id==='stale-result'?'#threshold':id==='form-recovery'?'#name':'a.skip');
await check(id,'keyboard focus indicator',async()=>assert.equal(await p.evaluate(()=>{let s=getComputedStyle(document.activeElement);return s.outlineStyle!=='none'&&parseFloat(s.outlineWidth)>=2}),true));
await p.screenshot({path:path.join(base,label+'-'+id+'-desktop.png'),fullPage:true});
for(const width of [320,640]){await p.setViewportSize({width,height:900});await check(id,'page reflow '+width,async()=>{assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'page-level horizontal overflow')});}
await p.setViewportSize({width:320,height:900});await audit(p,id,'320px');
if(['create-triage','dense-expert','chart-equivalent'].includes(id)){let s=id==='create-triage'?'.table-wrap':id==='dense-expert'?'.table-region':'.chart-scroll';await open();await check(id,'keyboard horizontal scroll at 320px',async()=>{await keyboardTo(p,s);let before=await p.locator(s).evaluate(e=>e.scrollLeft);await p.keyboard.press('ArrowRight');await p.waitForTimeout(250);let after=await p.locator(s).evaluate(e=>e.scrollLeft);assert.ok(after>before,'ArrowRight did not scroll the comparison region')})}
await p.screenshot({path:path.join(base,label+'-'+id+'-320.png'),fullPage:true});
await open();await p.setViewportSize({width:640,height:900});
// Explicit text-enlargement simulation: double computed fonts without scaling the viewport.
await p.evaluate(()=>{let es=[...document.querySelectorAll('body *')].filter(e=>!e.closest('svg')&&!['SCRIPT','STYLE'].includes(e.tagName));let sizes=es.map(e=>parseFloat(getComputedStyle(e).fontSize));es.forEach((e,i)=>e.style.fontSize=sizes[i]*2+'px');document.body.style.fontSize=parseFloat(getComputedStyle(document.body).fontSize)*2+'px'});
await check(id,'200% text page reflow',async()=>assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'page overflow with doubled text'));
await p.screenshot({path:path.join(base,label+'-'+id+'-text200.png'),fullPage:true});
fs.writeFileSync(path.join(base,label+'-'+id+'-accessibility.yml'),await p.locator('body').ariaSnapshot());
await check(id,'main controls have usable hit areas',async()=>{let sizes=await p.locator('button,input,select').evaluateAll(es=>es.filter(e=>e.getClientRects().length).map(e=>{let r=e.getBoundingClientRect();return {id:e.id,width:r.width,height:r.height}}));assert.ok(sizes.every(r=>r.width>=24&&r.height>=24),JSON.stringify(sizes))});
await context.close();
const touch=await browser.newContext({viewport:{width:375,height:812},hasTouch:true,isMobile:true}),tp=await touch.newPage();await tp.goto(pathToFileURL(path.join(base,id+'.html')).href);
await check(id,'touch primary action at 375px',async()=>{
if(id==='create-triage'){await tp.locator('[data-action="claim"]').tap();await text(tp,'#status',/claimed locally/)}
if(id==='dense-expert'){await tp.locator('#inspect').tap();assert.ok(await tp.locator('#invoice').isVisible());await tp.locator('#close-invoice').tap();assert.equal(await tp.locator('#invoice').isVisible(),false)}
if(id==='expressive-brand'){await tp.locator('#name').fill('Alex');await tp.locator('#email').fill('alex@example.com');await tp.locator('button[type="submit"]').tap();assert.ok(await tp.locator('#summary').isVisible());await tp.locator('#clear').tap();assert.equal(await tp.locator('#name').inputValue(),'')}
if(id==='truthful-demo'){await tp.locator('#analyze').tap();await text(tp,'#mean',/^4$/)}
if(id==='stale-result'){await tp.locator('#threshold').fill('15');await tp.locator('button[type="submit"]').tap();await text(tp,'#result',/1 of 3/)}
if(id==='chart-equivalent'){assert.deepEqual(await tp.locator('tbody td').allTextContents(),['18','25','21','30','24','16']);assert.ok(await tp.locator('table').isVisible())}
if(id==='form-recovery'){await tp.locator('#email').fill('alex@example.com');await tp.locator('#submit').tap();await text(tp,'#status',/No data was sent/)}
});await touch.close();}
const result={method:'Real headless Chromium; Playwright keyboard/pointer and rendering; axe automated accessibility. 200% text is computed-font doubling, not browser zoom or user testing.',browser:await browser.version(),checks,audits,errors,external_requests:requests};fs.writeFileSync(path.join(base,label+'-browser-results.json'),JSON.stringify(result,null,2)+'\n');await browser.close();console.log(JSON.stringify({checks:checks.length,failed:checks.filter(x=>x.result==='fail'),errors,requests},null,2));}
main().catch(e=>{console.error(e);process.exit(1)});
