document.querySelectorAll('.scroll-wrapper').forEach(wrapper => {
    const leftBtn = wrapper.querySelector('.scroll-button.left');
    const rightBtn = wrapper.querySelector('.scroll-button.right');
    const container = wrapper.querySelector('.cards-container');

    // Set the desired scroll amount (in pixels)
    const scrollAmount = 500;

    leftBtn.addEventListener('click', () => {
        container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    rightBtn.addEventListener('click', () => {
        container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
});
