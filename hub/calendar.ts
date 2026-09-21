export const START='2026-09-22';
export const END='2027-01-15';
export function isoDate(d:Date){return d.toISOString().slice(0,10)}
export function dayDate(s:string){return new Date(s+'T12:00:00Z')}
export function excluded(s:string){return dayDate(s).getUTCDay()===0||(s>='2026-11-06'&&s<='2026-11-15')||(s>='2026-12-15'&&s<='2026-12-21')}
export function studyDates(start=START,count=198){const out:string[]=[];const d=dayDate(start);while(out.length<count){const s=isoDate(d);if(!excluded(s))out.push(s);d.setUTCDate(d.getUTCDate()+1)}return out}
export const prepDates=studyDates().filter(d=>d<=END);
export const readingDates=studyDates(START,196);
export const formatDate=(s:string)=>dayDate(s).toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric',timeZone:'UTC'});
