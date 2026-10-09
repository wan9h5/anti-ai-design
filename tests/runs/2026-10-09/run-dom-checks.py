"""Reproduce synthetic DOM checks. Requires Node and jsdom; does not launch a browser.
Usage: python run-dom-checks.py --jsdom /absolute/path/to/node_modules/jsdom
"""
import argparse, json, subprocess, pathlib
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--jsdom',required=True);a=p.parse_args()
base=pathlib.Path(__file__).resolve().parent
js=r'''
const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const {JSDOM,VirtualConsole}=require(process.argv[1]);const base=process.argv[2];
const records=[];const errors=[];
function open(id){let vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push({scenario:id,error:e.message}));let dom=new JSDOM(fs.readFileSync(path.join(base,id+'.html'),'utf8'),{runScripts:'dangerously',url:'https://synthetic.example/',virtualConsole:vc});let d=dom.window.document;return {dom,d,w:dom.window,q:s=>d.querySelector(s),text:()=>d.body.textContent};}
function test(id,name,fn){try{fn();records.push({scenario:id,check:name,result:'pass'});}catch(e){records.push({scenario:id,check:name,result:'fail',error:e.message});}}
function input(o,id,value,type='input'){o.q('#'+id).value=value;o.q('#'+id).dispatchEvent(new o.w.Event(type,{bubbles:true}));}
function submit(o,selector){o.q(selector).dispatchEvent(new o.w.Event('submit',{bubbles:true,cancelable:true}));}
let o=open('create-triage');
test('create-triage','three records and critical-first comparison',()=>{assert.equal(o.q('#incidents').children.length,3);assert.match(o.q('#incidents tr').textContent,/INC-01/)});
test('create-triage','severity filter',()=>{input(o,'severity','warning','change');assert.equal(o.q('#incidents').children.length,1);assert.match(o.q('#incidents').textContent,/INC-02/)});
test('create-triage','claim updates owner and preserves useful focus when row disappears',()=>{input(o,'severity','all','change');input(o,'owner','unowned','change');let b=o.q('[data-action="claim"]');b.focus();b.click();assert.match(o.q('#status').textContent,/claimed locally/);assert.match(o.q('#incidents').textContent,/No matching/);assert.equal(o.d.activeElement.id,'owner')});
test('create-triage','empty recovery and release',()=>{o.q('#empty-clear').click();assert.equal(o.d.activeElement.id,'clear');let b=o.q('[data-action="release"]');assert.ok(b);b.click();assert.match(o.q('#incidents').textContent,/Unowned/);assert.equal(o.d.activeElement.dataset.action,'claim')});
test('create-triage','reset and local-only disclosure',()=>{o.q('[data-action="claim"]').click();o.q('#reset').click();assert.ok(o.q('[data-action="claim"]'));assert.match(o.text(),/no production service|no production/i);assert.match(o.text(),/page reload/i)});
o.dom.window.close();o=open('dense-expert');
test('dense-expert','all seven columns and both rows retained',()=>{assert.equal(o.d.querySelectorAll('thead th').length,7);assert.equal(o.d.querySelectorAll('tbody tr').length,2);for(let s of ['AC-01','AC-02','Ada','Lin','−20.00','800.00'])assert.ok(o.text().includes(s))});
test('dense-expert','resolve and undo preserve discrepancy',()=>{o.q('#resolve').click();assert.equal(o.q('#ac01-status').textContent,'Resolved');assert.match(o.q('#feedback').textContent,/−20.00/);o.q('#resolve').click();assert.equal(o.q('#ac01-status').textContent,'Review')});
test('dense-expert','invoice open close and programmatic focus restoration',()=>{o.q('#inspect').click();assert.equal(o.q('#invoice').hidden,false);assert.equal(o.q('#inspect').getAttribute('aria-expanded'),'true');assert.equal(o.d.activeElement.id,'close-invoice');o.q('#close-invoice').click();assert.equal(o.q('#invoice').hidden,true);assert.equal(o.d.activeElement.id,'inspect')});
test('dense-expert','Escape handler closes invoice',()=>{o.q('#inspect').click();o.q('#invoice').dispatchEvent(new o.w.KeyboardEvent('keydown',{key:'Escape',bubbles:true,cancelable:true}));assert.equal(o.q('#invoice').hidden,true);assert.equal(o.d.activeElement.id,'inspect')});
test('dense-expert','scroll region reachable and overflow declared in CSS',()=>{assert.equal(o.q('.table-region').tabIndex,0);assert.match(o.q('style').textContent,/overflow:\s*auto/);assert.match(o.q('style').textContent,/tabular-nums/)});
o.dom.window.close();o=open('expressive-brand');
test('expressive-brand','warm gradient and serif brand preserved in source',()=>{assert.match(o.q('style').textContent,/linear-gradient/);assert.match(o.q('style').textContent,/Georgia/);for(let s of ['Night','Print','Studio Hall','14 November','18:00–21:00','30'])assert.ok(o.text().includes(s))});
test('expressive-brand','empty name retained and actionable validation focused',()=>{input(o,'email','alex@example.com');submit(o,'#registration-form');assert.equal(o.q('#email').value,'alex@example.com');assert.equal(o.q('#name').getAttribute('aria-invalid'),'true');assert.equal(o.d.activeElement.id,'name')});
test('expressive-brand','invalid email association and retained name',()=>{input(o,'name','Alex');input(o,'email','bad');submit(o,'#registration-form');assert.equal(o.q('#name').value,'Alex');assert.equal(o.d.activeElement.id,'email');assert.match(o.q('#email-error').textContent,/email address/)});
test('expressive-brand','registration preview with no reservation claim',()=>{input(o,'email','alex@example.com');submit(o,'#registration-form');assert.equal(o.q('#summary').hidden,false);assert.equal(o.q('#registration-form').hidden,true);assert.equal(o.q('#result-name').textContent,'Alex');assert.match(o.q('#result-status').textContent,/No reservation/);assert.equal(o.d.activeElement.id,'summary-title')});
test('expressive-brand','edit and clear recovery',()=>{o.q('#edit').click();assert.equal(o.q('#name').value,'Alex');submit(o,'#registration-form');o.q('#clear').click();assert.equal(o.q('#name').value,'');assert.equal(o.q('#email').value,'');assert.equal(o.d.activeElement.id,'name')});
o.dom.window.close();o=open('truthful-demo');
test('truthful-demo','action/result explicitly disclose no AI backend',()=>{assert.match(o.q('#boundary').textContent,/no AI model or backend/);assert.match(o.q('.mode').textContent,/no AI execution/)});
test('truthful-demo','SYN-01 arithmetic and provenance',()=>{o.q('#analyze').click();assert.equal(o.q('#mean').textContent,'4');assert.equal(o.q('#range').textContent,'4');assert.match(o.q('#provenance').textContent,/SYN-01/);assert.equal(o.q('#future').hidden,false)});
test('truthful-demo','input change clears prior visible summary',()=>{input(o,'sample','SYN-02','change');assert.equal(o.q('#output').hidden,true);assert.equal(o.q('#future').hidden,true)});
test('truthful-demo','SYN-02 arithmetic',()=>{o.q('#analyze').click();assert.equal(o.q('#mean').textContent,'3');assert.equal(o.q('#range').textContent,'0');assert.match(o.q('#status').textContent,/AI analysis was not run/)});
test('truthful-demo','invalid fixture recovers without false execution',()=>{input(o,'sample','UNKNOWN','change');o.q('#analyze').click();assert.equal(o.q('#output').hidden,true);assert.match(o.q('#status').textContent,/Unknown sample/)});
o.dom.window.close();o=open('stale-result');
test('stale-result','original saved run retained with threshold',()=>{assert.match(o.q('#history-body').textContent,/DEMO-01/);assert.match(o.q('#run-detail').textContent,/threshold 10/);assert.match(o.q('#result').textContent,/2 of 3/)});
test('stale-result','editing threshold marks previous result without recomputation',()=>{input(o,'threshold','15');assert.match(o.q('#status').textContent,/Previous result/);assert.match(o.q('#status').textContent,/report uses threshold 10/);assert.match(o.q('#result').textContent,/2 of 3/)});
test('stale-result','rerun updates result and preserves history',()=>{submit(o,'#form');assert.match(o.q('#result').textContent,/1 of 3.*threshold 15/);assert.equal(o.q('#history-body').children.length,2);assert.match(o.q('#history-body').textContent,/DEMO-01/);assert.match(o.q('#run-detail').textContent,/DEMO-02/)});
test('stale-result','blank rejected instead of coerced to zero',()=>{input(o,'threshold','');submit(o,'#form');assert.equal(o.q('#input-error').hidden,false);assert.equal(o.q('#history-body').children.length,2);assert.equal(o.d.activeElement.id,'threshold');assert.match(o.q('#result').textContent,/threshold 15/)});
test('stale-result','equality exclusion and zero matches',()=>{input(o,'threshold','12');submit(o,'#form');assert.match(o.q('#result').textContent,/1 of 3/);input(o,'threshold','20');submit(o,'#form');assert.match(o.q('#result').textContent,/0 of 3/);assert.match(o.q('#scope').textContent,/No values/)});
test('stale-result','returning to latest threshold makes result current',()=>{input(o,'threshold','10');assert.match(o.q('#status').textContent,/Previous/);input(o,'threshold','20');assert.match(o.q('#status').textContent,/Current/)});
o.dom.window.close();o=open('form-recovery');
test('form-recovery','invalid input retains both fields and associates error',()=>{input(o,'name','Alex');input(o,'email','bad');submit(o,'#form');assert.equal(o.q('#name').value,'Alex');assert.equal(o.q('#email').value,'bad');assert.equal(o.q('#email').getAttribute('aria-invalid'),'true');assert.match(o.q('#email').getAttribute('aria-describedby'),/email-error/);assert.equal(o.d.activeElement.id,'email')});
test('form-recovery','outage distinct from input error and offers retry',()=>{input(o,'email','alex@example.com');input(o,'service','Outage','change');submit(o,'#form');assert.equal(o.q('#status').dataset.state,'service');assert.match(o.q('#status').textContent,/service outage/);assert.equal(o.q('#email-error').hidden,true);assert.equal(o.q('#email').value,'alex@example.com');assert.match(o.q('#submit').textContent,/Retry/)});
test('form-recovery','retry retains data during repeated outage',()=>{submit(o,'#form');assert.equal(o.q('#name').value,'Alex');assert.equal(o.q('#status').dataset.state,'service')});
test('form-recovery','available recovery success remains local',()=>{input(o,'service','Available','change');submit(o,'#form');assert.equal(o.q('#status').dataset.state,'success');assert.match(o.q('#status').textContent,/No data was sent or saved/);assert.equal(o.q('#email').value,'alex@example.com')});
test('form-recovery','editing clears stale success',()=>{input(o,'name','Alex changed');assert.equal(o.q('#status').textContent,'')});
// Chart is intentionally inspected as an equivalent-data view, not rendered pixels.
if(fs.existsSync(path.join(base,'chart-equivalent.html'))){o=open('chart-equivalent');test('chart-equivalent','six exact monthly counts in semantic table',()=>{let rows=[...o.d.querySelectorAll('table tbody tr')];assert.equal(rows.length,6);assert.deepEqual(rows.map(r=>Number(r.querySelector('td').textContent)),[18,25,21,30,24,16]);});test('chart-equivalent','chart has accessible name and synthetic source disclosure',()=>{assert.ok(o.q('svg[aria-labelledby],svg[aria-label],canvas[aria-label]'));assert.match(o.text(),/synthetic|demo/i);assert.match(o.text(),/2026/);assert.match(o.text(),/incident/i)});o.dom.window.close();}
console.log(JSON.stringify({method:'Node + jsdom, no rendering/browser; synthetic events and programmatic focus only',checks:records,script_errors:errors},null,2));
'''
r=subprocess.run(['node','-e',js,a.jsdom,str(base)],text=True,capture_output=True)
if r.returncode:raise SystemExit(r.stderr)
result=json.loads(r.stdout);(base/'dom-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':len(result['checks']),'failed':[c for c in result['checks'] if c['result']=='fail'],'script_errors':result['script_errors']},indent=2))
