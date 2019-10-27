const modal = document.querySelector(".modal");
const closeModal = document.querySelector(".close-modal");
const enquiry = document.querySelector("#enquiry");

enquiry.addEventListener('click', () => {
    modal.style.display = "block";
});

closeModal.addEventListener('click', () => {
    modal.style.display = "none";
});