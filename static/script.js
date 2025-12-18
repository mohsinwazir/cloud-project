document.addEventListener('DOMContentLoaded', () => {
    // Filter Logic
    const filterBtns = document.querySelectorAll('.filter-btn');
    const products = document.querySelectorAll('.product-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active to clicked
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            products.forEach(product => {
                if (filterValue === 'all' || product.getAttribute('data-category') === filterValue) {
                    product.style.display = 'flex';
                } else {
                    product.style.display = 'none';
                }
            });
        });
    });

    // Cart Logic
    let cart = JSON.parse(localStorage.getItem('cloudShopCart')) || [];
    updateCartCount();

    window.addToCart = function(name, price) {
        cart.push({ name, price });
        localStorage.setItem('cloudShopCart', JSON.stringify(cart));
        updateCartCount();
        
        // Visual feedback
        const btn = event.currentTarget;
        const originalIcon = btn.innerHTML;
        btn.innerHTML = '<i class="fa-solid fa-check"></i>';
        btn.style.background = 'var(--success)';
        
        setTimeout(() => {
            btn.innerHTML = originalIcon;
            btn.style.background = '';
        }, 1000);
    };

    function updateCartCount() {
        const count = document.getElementById('cart-count');
        if (count) {
            count.innerText = cart.length;
        }
    }
});
