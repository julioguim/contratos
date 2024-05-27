document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const searchIcon = document.getElementById('search-icon');

    searchInput.addEventListener('input', function() {
        const searchText = this.value.toLowerCase().trim();
        const rows = document.querySelectorAll('tbody tr');

        rows.forEach(row => {
            const columns = row.getElementsByTagName('td');
            let found = false;

            Array.from(columns).forEach(column => {
                const text = column.textContent.toLowerCase().trim();
                if (text.includes(searchText)) {
                    found = true;
                }
            });

            if (found) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
});