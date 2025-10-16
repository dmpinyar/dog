import { useState, useEffect } from "react";
import { getProgress } from "../api/horse_race";

export default function App() {
  interface prog {
    active: boolean;
    year: number;
    month: number;
    day: number;
  }

  const [prog, setProg] = useState<prog | null>(null);

  useEffect(() => {
    const fetchProgress = async () => {
      const data = await getProgress();
      if (JSON.stringify(data) !== JSON.stringify(prog)) {
        setProg(data);
      }
    }

    fetchProgress();
    const interval = setInterval(fetchProgress, 10000); // in milliseconds
    return () => clearInterval(interval);
  }, []);

  return (
    <>{prog ? (<p>{prog.month}/{prog.day}/{prog.year}</p>) : (<p>Loading...</p>)}</>
  );

}

