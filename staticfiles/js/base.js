const scrollLeftBtn = document.getElementById('scrollLeft');
const scrollRightBtn = document.getElementById('scrollRight');
const cardsContainer = document.getElementById('cardsContainer');

// Adjust scroll amount as needed
const scrollAmount = 300;

scrollLeftBtn.addEventListener('click', () => {
    cardsContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
});

scrollRightBtn.addEventListener('click', () => {
    cardsContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
});
