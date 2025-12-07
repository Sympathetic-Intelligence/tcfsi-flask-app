_j(function() {
	_j(document).on("click","header a", function(e){
		// keeps the page from sliding when a menu item is clicked
		e.stopPropagation()
	})

	const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
	const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
	

	_j(document).on("click", ".nav-link", function(){
		let activeTab = _j(this).attr("id")
		let t = activeTab.split("-")[1].charAt(4)
		//.charAt(str.length-1)

		let illustrations = ["tier-1-painter","tier-2-violin","tier-3-crowd"]
		_j(".tier-illustration").removeClass(illustrations)
		_j(".tier-illustration").addClass(illustrations[t-1])
	})
	
	/// get url parameters
	function GetURLParameter(sParam){
    
	  var searchParams = new URLSearchParams(window.location.search)
	  return searchParams.get(sParam)

	}
	if (GetURLParameter('theme')){
		let theme = GetURLParameter('theme')
		_j('html').attr('data-bs-theme',theme)

	} 

	var pathArray = window.location.pathname.split('/');
	var curr_page = pathArray[1]

	if (curr_page != ''){
		_j('.navbar .nav-link').removeClass('active')
		_j('#'+curr_page).addClass('active')
	}
	


	if (GetURLParameter('tier')){
		let tier = GetURLParameter('tier')

		_j(".nav-tabs .nav-link").removeClass('active')
		_j("#nav-tier"+tier+"-tab").addClass('active')

		_j(".tab-pane").removeClass('active show')
		_j("#nav_tier"+tier).addClass('active show')

		_j("#nav-tier"+tier+"-tab").trigger('click')
	}
	
	_j(".tier-illustration").on('click',function(){
		location.href = '/concept_home?theme=concept';
	})
	// _j(".banner.top").on('click',function(){
	// 	location.href = '/sos?theme=center';
	// })
	_j(".banner.bottom").on('click',function(){
		location.href = '/little_book?theme=center';
	})



	// chek ip
	// _j.get("http://ipinfo.io", function(response) {
	// 	console.log(response);
	// 	console.log(response.country);
	// 	if (response.country == "US"){
	// 		location.href = '/sos?theme=center';
	// 	}
	// }, "jsonp");

});