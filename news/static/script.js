document.addEventListener("DOMContentLoaded", function() {
    const filterButtons = document.querySelectorAll(".filter-btn");
    const articles = document.querySelectorAll(".article-card");
    console.log(filterButtons, articles);
    
    filterButtons.forEach(button => {
        button.addEventListener("click", function() {
            const filterValue = this.getAttribute("data-filter");

            // Show all articles if 'All' is clicked
            if (filterValue === "all") {
                articles.forEach(article => article.style.display = "block");
            } else {
                articles.forEach(article => {
                    const categories = article.getAttribute("data-category").split(" ");
                    if (categories.includes(filterValue)) {
                        article.style.display = "block";
                    } else {
                        article.style.display = "none";
                    }
                });
            }

            // Update button active state
            filterButtons.forEach(btn => btn.classList.remove("active"));
            this.classList.add("active");
        });
    });
});
