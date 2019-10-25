const modal = document.querySelector(".modal");
const enquiry = document.querySelector("#enquiry");

enquiry.addEventListener('click', () => {
    modal.style.display = "block";
});

modal.addEventListener('click', () => {
    modal.style.display = "none";
});