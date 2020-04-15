//var i;
//for (i = 0; i < "//I need this to be the max amount of items in my list"; i++) {
//
//  document.getElementById("hide-image-" + i).addEventListener("click", imageToggleHide);
//    document.getElementById("show-image-" + i).addEventListener("click", imageToggleShow);
//
//    function imageToggleHide() {
//        document.getElementById("card-image-test-" + i).style.display = "none";
//    };

//    function imageToggleShow() {
//        document.getElementById("card-image-test-" + i).style.display = "block";
//    };
//}

function imageToggleHide(the_id) {
        document.getElementById(the_id).style.display = "none";
    };

function imageToggleShow(the_id) {
        document.getElementById(the_id).style.display = "block";
    };