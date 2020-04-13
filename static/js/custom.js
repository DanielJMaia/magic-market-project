var i;
for (i = 0; i < 2; i++) {

    document.getElementById("hide-image-" + i).addEventListener("click", imageToggleHide);
    document.getElementById("show-image-" + i).addEventListener("click", imageToggleShow);

    function imageToggleHide() {
        document.getElementById("card-image-test-" + i).style.display = "none";
    };

    function imageToggleShow() {
        document.getElementById("card-image-test-" + i).style.display = "block";
    };
}