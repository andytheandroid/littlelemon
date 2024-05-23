const tabs = document.querySelectorAll('.tab-content');
const tabLinks = document.querySelectorAll('.tabs a');

tabLinks.forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();

        tabs.forEach(tab => tab.classList.remove('active'));
        tabLinks.forEach(link => link.classList.remove('active'));

        const targetId = link.getAttribute('href');
        document.querySelector(targetId).classList.add('active');
        link.classList.add('active');
    });
});

// Show the first tab by default (if needed)
document.querySelector('.tab-content').classList.add('active');