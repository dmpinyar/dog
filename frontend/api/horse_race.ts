const API_BASE = "/api/horse_race/"; 
const INSTANT_BASE = "/api/horse_instant"

export async function getProgress() {
  const res = await fetch(API_BASE);
  return res.json();
}

// export async function saveProgress(progress: { active: boolean,
//     year: number, month: number, day: number, horses: number,
//     time: number }) {

//     const res = await fetch(API_BASE, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(progress),
//   });
//   return res.json();
// }

export async function getInstantiation() {
  const res = await fetch(INSTANT_BASE);
  return res.json();
}