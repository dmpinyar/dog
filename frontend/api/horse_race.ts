const API_BASE = "/api/horse_race/"; 
const INSTANT_BASE = "/api/horse_instant"

export async function getProgress() {
  const res = await fetch(API_BASE);
  return res.json();
}

export async function getInstantiation() {
  const res = await fetch(INSTANT_BASE);
  return res.json();
}