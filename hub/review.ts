export type Review = {status:'Not started'|'Shaky'|'Solid';fragile:boolean;core:boolean;stage:number;due:string;last:string;active:boolean;checks:boolean[];notes:string;history:{date:string;rating:string}[]};
export const NORMAL=[1,3,7,21], FRAGILE=[1,2,5,14,30];
export function todayLocal(d=new Date()){return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`}
function validDate(s:unknown):s is string{return typeof s==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(s)&&Number.isFinite(Date.parse(s))&&new Date(s+'T12:00:00Z').toISOString().slice(0,10)===s}
export function addDays(s:string,n:number){if(!validDate(s))throw Error('Invalid review date');const d=new Date(s+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10)}
export function freshReview(core=false):Review{return {status:'Not started',fragile:false,core,stage:-1,due:'',last:'',active:false,checks:[false,false,false],notes:'',history:[]}}
export function readReview(raw:unknown,core=false):Review{
 if(raw===undefined)return freshReview(core);
 if(typeof raw!=='string')throw Error('Invalid topic record');const r=JSON.parse(raw);
 if(!r||!['Not started','Shaky','Solid'].includes(r.status)||typeof r.fragile!=='boolean'||typeof r.core!=='boolean'||!Number.isInteger(r.stage)||r.stage< -1||r.stage>(r.fragile?4:3)||typeof r.active!=='boolean'||!Array.isArray(r.checks)||r.checks.length!==3||r.checks.some((x:unknown)=>typeof x!=='boolean')||typeof r.notes!=='string'||r.notes.length>12000||!Array.isArray(r.history)||r.history.length>20||!['due','last'].every(k=>r[k]===''||validDate(r[k]))||r.history.some((x:{date:unknown;rating:unknown})=>!x||!validDate(x.date)||!['Shaky','Solid'].includes(String(x.rating))))throw Error('Invalid topic record');
 return r as Review;
}
export function startReview(r:Review):Review{return {...r,active:true,checks:[false,false,false]}}
export function isDue(r:Review,day:string){return !!r.due&&r.due<=day}
export function finishReview(r:Review,rating:'Shaky'|'Solid',day:string):Review{
 if(!validDate(day)||!r.active||!r.checks.every(Boolean))throw Error('Attempt all three prompts in a fresh review first');
 const gaps=r.fragile?FRAGILE:NORMAL;
 // Early practice can diagnose failure, but cannot earn repeated stage advances.
 const advance=!r.due||isDue(r,day);
 const stage=rating==='Shaky'?0:advance?Math.min(r.stage+1,gaps.length-1):r.stage;
 const due=rating==='Solid'&&!advance?r.due:addDays(day,gaps[Math.max(0,stage)]);
 return {...r,status:rating,stage,due,last:day,active:false,history:[...r.history,{date:day,rating}].slice(-20)};
}
export function setFragile(r:Review,fragile:boolean):Review{
 const gaps=fragile?FRAGILE:NORMAL,stage=Math.min(r.stage,gaps.length-1);
 const candidate=r.last&&stage>=0?addDays(r.last,gaps[stage]):'';
 return {...r,fragile,stage,due:fragile&&candidate&&r.due?([candidate,r.due].sort()[0]):r.due};
}
export function validateTopicFields(data:Record<string,unknown>){for(const [key,value] of Object.entries(data))if(key.startsWith('topic:'))readReview(value);}
