//JavaScript for modal implementation

/****************** Modal and button variables ************************/
const modal = document.querySelector(".modal");
const closeModal = document.querySelector(".close-modal");
const enquiry = document.querySelector("#enquiry");

// add an event listener to the button
enquiry.addEventListener('click', () => {
    //when the button is clicked, show the modal and its contents
    modal.style.display = "block";
});

// add event listener to close modal button
closeModal.addEventListener('click', () => {
    //when the button is clicked, remove the modal and its contents
    modal.style.display = "none";
});