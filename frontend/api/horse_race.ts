const API_BASE = "/api/horse_race/"; 

export async function getProgress() {
  const res = await fetch(API_BASE);
  return res.json();
}