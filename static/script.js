document.addEventListener("DOMContentLoaded", function () {
    const resultDiv = document.getElementById("result");
    const larvaeCount = document.getElementById("larvae-count");
    const processedImage = document.getElementById("processed-image");
    const progressBar = document.getElementById("bar");

    // Hide result initially
    resultDiv.style.display = "none";

    const form = document.querySelector("form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Hide form and show result div
        form.style.display = "none";
        resultDiv.style.display = "block";

        const formData = new FormData(form);

        const response = await fetch("/process", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();

            // Update the larvae count and display the processed image
            larvaeCount.textContent = result.count;
            processedImage.src = result.processedImage;

            // Hide the progress bar
            progressBar.style.width = "100%";
        } else {
            larvaeCount.textContent = "Error processing image.";
        }
    });
});
