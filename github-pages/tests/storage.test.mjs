import {test} from 'node:test';
import assert from 'node:assert/strict';
import {loadBrowserProgress,saveBrowserRecord,saveBrowserStart,parseBackup,restoreBrowserProgress,STORAGE_KEY} from '../../lib/browser-progress.ts';
const ids=['word2vec','alexnet'];
const store=()=>{const m=new Map();return {getItem:k=>m.get(k)??null,setItem:(k,v)=>m.set(k,v)}};
const note={status:'Read',confidence:4,notes:{summary:'हिन्दी notes: context → word'}};
test('notes and shifted dates survive a new load and backup round trip',()=>{
 const s=store();saveBrowserRecord(s,ids,'word2vec',note);saveBrowserStart(s,ids,'2026-09-28');
 const loaded=loadBrowserProgress(s,ids);assert.deepEqual(loaded.records.word2vec,note);assert.equal(loaded.start,'2026-09-28');
 const restored=store();restoreBrowserProgress(restored,ids,parseBackup(JSON.stringify(loaded),ids));assert.deepEqual(loadBrowserProgress(restored,ids),loaded);
});
test('successive saves preserve the other paper',()=>{const s=store();saveBrowserRecord(s,ids,'word2vec',note);saveBrowserRecord(s,ids,'alexnet',{...note,status:'Reading'});assert.equal(Object.keys(loadBrowserProgress(s,ids).records).length,2)});
test('invalid dates and backups cannot replace existing data',()=>{
 const s=store();saveBrowserRecord(s,ids,'word2vec',note);const before=s.getItem(STORAGE_KEY);
 assert.throws(()=>saveBrowserStart(s,ids,'2026-02-30'));assert.throws(()=>parseBackup('{"version":2}',ids));
 assert.throws(()=>restoreBrowserProgress(s,ids,{version:1,start:'2026-09-20',records:{unknown:note}}));
 assert.throws(()=>restoreBrowserProgress(s,ids,{version:1,start:'2026-09-20',records:{word2vec:{...note,confidence:7}}}));assert.equal(s.getItem(STORAGE_KEY),before);
});
test('quota failure reports unsaved changes and preserves existing data',()=>{
 const s=store();saveBrowserRecord(s,ids,'word2vec',note);const before=s.getItem(STORAGE_KEY);
 assert.throws(()=>saveBrowserStart({...s,setItem:()=>{throw Error('quota')}},ids,'2027-01-01'),/not saved/);assert.equal(s.getItem(STORAGE_KEY),before);
});
test('corrupt stored data is not silently overwritten',()=>{const s=store();s.setItem(STORAGE_KEY,'bad json');assert.throws(()=>saveBrowserRecord(s,ids,'word2vec',note));assert.equal(s.getItem(STORAGE_KEY),'bad json')});
