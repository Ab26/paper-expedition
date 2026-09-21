export type ReadingRecord = {status:string; confidence:number; notes:Record<string,string>};
export type Backup = {version:1; start:string; records:Record<string,ReadingRecord>};
type Store = Pick<Storage,'getItem'|'setItem'>;
export const STORAGE_KEY='paper-expedition:paper-expedition:v1';
const statuses=['Not started','Reading','Read','Revisit'];
const own=(value:unknown):value is Record<string,unknown>=>value!==null&&typeof value==='object'&&!Array.isArray(value);
const validDate=(s:unknown):s is string=>typeof s==='string'&&/^20\d{2}-\d{2}-\d{2}$/.test(s)&&Number.isFinite(Date.parse(s))&&new Date(s).toISOString().slice(0,10)===s;

export function parseBackup(raw:string,ids:string[]):Backup {
 const data:unknown=JSON.parse(raw);
 if(!own(data)||data.version!==1||!validDate(data.start)||!own(data.records))throw Error('This is not a valid Paper Expedition backup.');
 const allowed=new Set(ids);const records:Record<string,ReadingRecord>={};
 for(const [id,value] of Object.entries(data.records)){
  if(!allowed.has(id)||!own(value)||typeof value.status!=='string'||!statuses.includes(value.status)||!Number.isInteger(value.confidence)||Number(value.confidence)<0||Number(value.confidence)>5||!own(value.notes))throw Error('Backup contains an invalid paper record.');
  const notes:Record<string,string>={};
  for(const [key,note] of Object.entries(value.notes)){
   if(!/^[a-z][a-zA-Z0-9_]{0,49}$/.test(key)||['constructor','prototype','__proto__'].includes(key)||typeof note!=='string'||note.length>12000)throw Error('Backup contains invalid study notes.');
   notes[key]=note;
  }
  records[id]={status:value.status,confidence:Number(value.confidence),notes};
 }
 return {version:1,start:data.start,records};
}
export function loadBrowserProgress(store:Store,ids:string[]):Backup {
 const raw=store.getItem(STORAGE_KEY);
 return raw===null?{version:1,start:'2026-09-22',records:{}}:parseBackup(raw,ids);
}
export function restoreBrowserProgress(store:Store,ids:string[],data:Backup):Backup {
 const valid=parseBackup(JSON.stringify(data),ids);
 try{store.setItem(STORAGE_KEY,JSON.stringify(valid));}catch{throw Error('Browser storage is full or unavailable. Your changes were not saved. Download a backup before clearing any site data.');}
 return valid;
}
export function saveBrowserRecord(store:Store,ids:string[],id:string,value:ReadingRecord):Backup {
 const next=loadBrowserProgress(store,ids);
 next.records[id]=value;
 return restoreBrowserProgress(store,ids,next);
}
export function saveBrowserStart(store:Store,ids:string[],start:string):Backup {
 return restoreBrowserProgress(store,ids,{...loadBrowserProgress(store,ids),start});
}
