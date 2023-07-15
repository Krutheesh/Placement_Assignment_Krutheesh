import React from "react";
import Headerone from "../components/Headerone";
import Services from "../components/Services";
import Trusted from "../components/Trusted";
function Home() {
  return (
    <div>
      <div className="px-[10rem] space-y-[4rem] ">
        <Headerone heading={"K store"} />
        <Services />
       
      </div>
      <div className='bg-[#f2e6ff] px-[10rem] py-[5rem] my-[4rem]'>
        <Trusted/>
      </div>
    </div>
  );
}

export default Home;
