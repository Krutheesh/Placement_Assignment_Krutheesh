import React from "react";

function Contact() {
  return (
    <div>
      <h2 className="py-[2rem] text-center text-[1.5rem] text-gray-600">
        Contact page
      </h2>
      <iframe
      className="w-full h-[50vh]"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3800.4541300195865!2d78.09460086858498!3d17.723228821122703!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcc07c9700f9233%3A0xf6227053db3247da!2sJNTUH%20University%20College%20of%20Engineering%20Sultanpur!5e0!3m2!1sen!2sin!4v1689311592665!5m2!1sen!2sin"
        allowFullScreen=""
        loading="lazy"
        referrerPolicy="no-referrer-when-downgrade"
      ></iframe>
      <div className="">
        <form action="https://formspree.io/f/meqbqwqb" method="post" className="space-y-5 w-[25rem] m-auto  mt-[4rem] ">
          <input className="w-full border-2 p-1" type="text" name="username" placeholder="Username" required/>
          <br />
          <input className="w-full border-2 p-1" type="email" name ="email" placeholder="Email" required/>
          <br />
          <textarea className="w-full border-2 p-1" type='text' name="message" placeholder="enter message">
          </textarea>
          <br />
          <br />
          <button  className="bg-[#9933ff] text-white px-4 py-2">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default Contact;
