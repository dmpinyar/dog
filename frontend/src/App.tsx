import { useState, useEffect } from "react";
import { getProgress, getInstantiation } from "../api/horse_race";

const MAX_RECENT_LENGTH = 20

export default function App() {
  interface instant {
    startYear: number;
    startMonth: number; 
    startDay: number;
    endYear: number;
    endMonth: number; 
    endDay: number;
  }

  interface prog {
    active: boolean;
    year: number;
    month: number;
    day: number;
    horses: number;
    time: number;
  }

  const [prog, setProg] = useState<prog[]>([]);
  const [instant, setInstant] = useState<instant>();
  const [active, setActive] = useState<boolean>(false);

  useEffect(() => {
    getInstantiation().then(setInstant);
    getProgress().then(data => {
      if (!Array.isArray(data)) {
        data = [data];
        if (data.active)
          setProg(data)
      } else 
        setProg(data);
      setActive(data[0]?.active || false);  
    });
    //getProgress().then(setProg)
  }, []);

  useEffect(() => {
    const fetchProgress = async () => {
      getProgress().then(data => {
        if (!Array.isArray(data)) data = [data];
        setProg(data);
        setActive(data[0]?.active || false);
      });
      
      //let shouldSave = false;

      // setProg(prevProg => {
      //   const isNew = prevProg.length === 0 || data.day !== prevProg[0].day;
      //   if (data.active && isNew) {
      //     shouldSave = true;
      //     return [data, ...prevProg].slice(0, MAX_RECENT_LENGTH);
      //   }
      //   return prevProg;
      // });

      // if (shouldSave) {
      //   saveProgress(data).catch(console.error);
      // }
    }


    fetchProgress();
    const interval = setInterval(fetchProgress, 10000); // in milliseconds
    return () => clearInterval(interval);
  }, []);


  return (
    <body style={{background: "#d2b48c"}}>
      <div
        style={{
          display: "flex",       
          gap: "20px",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <div style={{
          background: "white",
          padding: "20px",
          width: "46vw",
          minHeight: "50vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          boxShadow: "0 0 10px rgba(0,0,0,0.1)",
          borderRadius: "10px",
        }}>
          {
            instant && active ? (
              <p>
                Currently scraping racingpost.com for horse data...
              <br></br> 
                Starting date:    {instant.startMonth}/{instant.startDay}/{instant.startYear} 
              <br></br> 
                Terminating date: {instant.endMonth}/{instant.endDay}/{instant.endYear} 
              <br></br>
                Current date:     {prog[0].month}/{prog[0].day}/{prog[0].year}!
              <br></br> 
                {prog[0].horses} horses raced today!
              <br></br> 
                It took about {prog[0].time} seconds to parse through today's data!
              </p>
            ) : (<p>The Server is not currently scraping...</p>)
          }
        </div>
        <div style={{
          background: "white",
          padding: "20px",
          width: "47vw",
          minHeight: "50vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          boxShadow: "0 0 10px rgba(0,0,0,0.1)",
          borderRadius: "10px",
        }}>
          <p>Here's the past twenty scraped days!
          <hr></hr>
          {
            <ol>
              {prog.map((data, index) => (
                <li key={index}>{data.month}/{data.day}/{data.year}: the process took {data.time} seconds, and {data.horses} horses ran!</li>
              ))}
            </ol>
          }
          </p>
        </div>
      </div>
    </body>
    

  );

}

