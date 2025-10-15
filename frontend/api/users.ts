const API_BASE = "/api/users"; // proxied through Apache

export async function getUsers() {
  const res = await fetch(API_BASE);
  return res.json();
}

export async function createUser(user: { name: string }) {
  const res = await fetch(API_BASE, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user),
  });
  return res.json();
}

