const button = document.getElementById("submit");
const idbox = document.getElementById("pass");
const name = document.getElementById("name");
const fname = document.getElementById("fname");
let canfire = true;
const urlofsend = "https://experimentihat01.aakashgudivada.repl.co/";

button.addEventListener("click", function() {
  if (idbox.value !== "" && canfire === true) {
    canfire = false;
    try {
      button.textContent = "Loading";
      const urlfornow = urlofsend + "post?id=" + idbox.value + "&sname=" + name.value + "&fname=" + fname.value;
      fetch(urlfornow)
      .then(response =>{
        console.log(response);
        alert("Saved");
        canfire = true;
        idbox.value = "";
        name.value = "";
        fname.value = "";
      })

    } catch (error) {
      console.log(error);
    }
  }else if (canfire === false){
    alert("A moment please, page is loading.");
  }else {
    alert("Fill the values of Student");
  }
});
