"use strict";

$(function() {

	// disclaimer: this code is ugly.
	 var sent = false;
        
	function setProposalStatus(id, value) {
		if (sent) {
			return;
		}
		sent = true;
		$(".accept-buttons,.unaccept").addClass('disabled');
		$.post('', {
			issue : id,
			accepted : value,
			unaccept : '1',
		}, function(data) {
			history.back();
		});
	}

	function do_vote(vote_url, vote_value, elem) {
		$.post(vote_url, {
			val : vote_value
		}, function(data) {
			if (data['result'] == 'ok') {
				var btn_div = elem.closest('div.vote-btns');
				btn_div.replaceWith(data['html']);
			}
		});
	}


	$(".proposal-action").click(function(event) {
		event.preventDefault();
		var el = $(this).closest('.proposal');
		setProposalStatus(el.data('id'), $(this).val());
		return false;
	});

	$(".unaccept").click(function(event) {
		event.preventDefault();
		var el = $(this).closest('.proposal');
		setProposalStatus(el.data('id'), $(this).data('value'));
		return false;
	});

	$(".container").on("click", "a[id|='vote']", function(event) {
		event.preventDefault();
		var vote_value = $(this).attr('id').substr(5);
		var target = $(this).attr('href');
		do_vote(target, vote_value, $(this));
	});



   $(".container").on("click", "a[id^='results']", function(event) {
      event.preventDefault();      
      var target = $(this).attr('href');
      var id = $('.piechart').data('prop-id')  
      $.get(target, function(data) {
          $('div.piechart').replaceWith(data)
          var pro = $('.piechart').data('pro')
          var con = $('.piechart').data('con')
          var total = $('.piechart').data('total')
          createChart(pro, con, total - (pro + con), id);

      })
 
   });

    
})