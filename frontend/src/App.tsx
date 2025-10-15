import { useState, useEffect } from "react";
import { getUsers, createUser } from "../api/users";

export default function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");

  useEffect(() => {
    getUsers().then(setUsers);
  }, []);

  const handleAddUser = async () => {
    if (!name.trim()) return;
    const newUser = await createUser({ name });
    setUsers([...users, newUser]);
    setName("");
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold">User Manager</h1>
      <input
        className="border p-2 mr-2"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter user name"
      />
      <button className="bg-blue-500 text-white px-3 py-2 rounded" onClick={handleAddUser}>
        Add User
      </button>

      <ul className="mt-4">
        {users.map((u: any) => (
          <li key={u.id}>{u.name}</li>
        ))}
      </ul>
    </div>
  );
}

