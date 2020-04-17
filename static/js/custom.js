function imageToggleHide(the_id) {
        document.getElementById(the_id).style.display = "none";
    };

function imageToggleShow(the_id) {
        document.getElementById(the_id).style.display = "block";
    };


// Stop the card carousels from working on the home page

$('.carousel').carousel({
    interval: false
}); 