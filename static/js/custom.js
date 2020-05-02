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

///This function changes the default boostrap transition duration
$(document).ready(function() {
  jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 500  // 500ms
});

//DataTables function

$(document).ready( function () {
    $('#all_cards').dataTable( {
    "order": [],
    "columnDefs": [ {
      "targets"  : 'no-sort',
      "orderable": false,
    }],
    "bFilter": false,
    lengthMenu: [10, 20, 50],
});
});

// django message fade-out
$(document).ready( function (){
    console.log("page loaded")
    $( "#message" ).fadeOut()
});
