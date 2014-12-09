$(function(){
	init(gallery);
	init(popup);
	init(arrows);
	// init(newstabs);
	init(autoslide);
});

$(window).resize(function(){
	setTimeout(function() {
		$('.content-gallery .slide-list ul, .gallery-list ul').css('marginLeft', 0);
	}, 1);
	footertobottom();
});

$(window).load(function () {
	footertobottom();
});

function init(f){
	if(f)f();
}

function footertobottom() {
	var docHeight = $(document).height();
	var winHeight = $(window).height();
	if (docHeight <= winHeight) {
		var wrapHeight = $('.wrapper-holder').height();
		$('.prop').height(winHeight-wrapHeight);
	}
}

function autoslide() {
	var delay=6000;
	var intervalID = setInterval(nextClick, delay);
	function nextClick() {
		var sumNum = $('.program-list li').size()-1;
		var curNum = $('.program-list li a.active').index('.program-list li a');
		if (curNum == sumNum) {
			$('.program-list li').first().find('a').click();
		} else {
			$('.program-list li').eq(curNum+1).find('a').click();
		}
	}
	$('.program-list li a').click(function(){
		clearTimeout(intervalID);
		intervalID = setInterval(nextClick, delay);
	});
}

function newstabs() {
	var numberDay = $('ul.choice-date li.active').index('ul.choice-date li');
	$('.news-list-box .news-list').hide();
	$('.news-list-box .news-list').eq(numberDay).show();
	$('ul.choice-date li a').click(function() {
		if ($(this).closest('li').attr('class') == 'active') {
			return false;
		} else {
			$('ul.choice-date li').removeClass('active');
			$(this).closest('li').addClass('active');
			numberDay = $(this).closest('li').index();
			$('.news-list-box .news-list').slideUp().eq(numberDay).slideDown();;
		}

		return false;
	});
}

function arrows() {
	$(".item-photo-group").each(function(){
		$(this).find('.item-photo-hldr').first().attr('data-end','first');
	 })
	$(".item-photo-group").each(function(){
		$(this).find('.item-photo-hldr').last().attr('data-end','last');
	 });

	$(".popup-holder .next").click(function() {
		var curNum = $(this).closest('.image').find('img').attr('src');
		$('a.photo[href="'+curNum+'"]').closest('.item-photo-hldr').next().find('a.photo').click();
		return false;
	});
	$(".popup-holder .prev").click(function() {
		var curNum = $(this).closest('.image').find('img').attr('src');
		$('a.photo[href="'+curNum+'"]').closest('.item-photo-hldr').prev().find('a.photo').click();
		return false;
	});

	$('a.photo').click(function() {
		$(".popup-holder .prev, .popup-holder .next").hide();
	});
	$('.item-photo-hldr a.photo').click(function() {
		$(".popup-holder .prev, .popup-holder .next").show();
		if ($(this).closest('.item-photo-hldr').attr('data-end')=='first') {
			$(".popup-holder .prev").hide();
		} else {
			if ($(this).closest('.item-photo-hldr').attr('data-end')=='last') {
				$(".popup-holder .next").hide();
			} else {
				$(".popup-holder .prev, .popup-holder .next").show();
			};
		};
	});
}
function gallery(){
	$('.promo-gallery').galleryScroll();
	$('.content-gallery').galleryScroll({
		holderList:'.slide-list',
		circleSlide: true
	})
	if('slider' in $.fn){
		$( ".slide-switcher" ).slider({
			min: 0,
			max: $('.promo-gallery .gallery-list>ul>li').size()-1,
			value:$('.promo-gallery .program-list .active').parent().index(),
			slide: function( event, ui ) {
				$('.promo-gallery .program-list li').eq(ui.value).find('a').trigger('click');
			}
		});
		$('.promo-gallery .program-list li').click(function(){
			$('.promo-gallery .title-list li').removeClass('active').eq($(this).index()).addClass('active');
			$( ".slide-switcher" ).slider('option','value',$(this).index())
		});
	}
}
function popup(){
	$('body').popup({
		"opener":".manager-list-holder .talk",
		"popup_holder":"#manager_connect_popup",
		"popup":".popup",
		"close_btn":".close"
	}).popup({
		"opener":".header-frame a.order-sound",
		"popup_holder":"#order_song_form",
		"popup":".popup",
		"close_btn":".close"
	}).popup({
		"opener":"",
		"popup_holder":".popup-holder:has(.text)",
		"popup":".popup",
		"close_btn":".close"
	}).popup({
		"opener":"a.photo",
		"popup_holder":".popup-holder:has(.image)",
		"popup":".popup",
		"close_btn":".close",
		"beforeOpen":function(popup_holder){
			$(popup_holder).find('img').attr('src',$(this).attr('href'));
		}
	});
}
jQuery.fn.galleryScroll = function(_options){
	var _options = jQuery.extend({
		btPrev: 'a.prev',
		btNext: 'a.next',
		holderList: '.gallery-list',
		scrollElParent: 'ul',
		scrollEl: 'li',
		slideNum: 'ul.program-list',
		duration : 1000,
		step: false,
		circleSlide: false,
		disableClass: 'disable',
		funcOnclick: null,
		autoSlide:false,
		innerMargin:0,
		stepWidth:false
	},_options);
	return this.each(function(){
		var _this = jQuery(this);
		var _holderBlock = jQuery(_options.holderList,_this);
		var _gWidth = _holderBlock.width();
		var _animatedBlock = jQuery(_options.scrollElParent,_holderBlock);
		var _liWidth = jQuery(_options.scrollEl,_animatedBlock).outerWidth(true);
		var _liSum = jQuery(_options.scrollEl,_animatedBlock).length * _liWidth;
		var _margin = -_options.innerMargin;
		var f = 0;
		var _step = 0;
		var _autoSlide = _options.autoSlide;
		var _timerSlide = null;
		if (!_options.step) _step = _gWidth; else _step = _options.step*_liWidth;
		if (_options.stepWidth) _step = _options.stepWidth;

		if (!_options.circleSlide) {
			if (_options.innerMargin == _margin)
				jQuery(_options.btPrev,_this).addClass('prev-'+_options.disableClass);
		}
		if (_options.slideNum && !_options.step) {
			var _lastSection = 0;
			var _sectionWidth = 0;
			while(_sectionWidth < _liSum)
			{
				_sectionWidth = _sectionWidth + _gWidth;
				if(_sectionWidth > _liSum) {
				       _lastSection = _sectionWidth - _liSum;
				}
			}
		}
		if (_autoSlide) {
				_timerSlide = setTimeout(function(){
					autoSlide(_autoSlide);
				}, _autoSlide);
			_animatedBlock.hover(function(){
				clearTimeout(_timerSlide);
			}, function(){
				_timerSlide = setTimeout(function(){
					autoSlide(_autoSlide)
				}, _autoSlide);
			});
		}
		jQuery(_options.btNext,_this).unbind('click');
		jQuery(_options.btPrev,_this).unbind('click');
		jQuery(_options.btNext,_this).bind('click',function(e){
			jQuery(_options.btPrev,_this).removeClass('prev-'+_options.disableClass);
			if (!_options.circleSlide) {
				if (_margin + _step  > _liSum - _gWidth - _options.innerMargin) {
					if (_margin != _liSum - _gWidth - _options.innerMargin) {
						_margin = _liSum - _gWidth  + _options.innerMargin;
						jQuery(_options.btNext,_this).addClass('next-'+_options.disableClass);
						_f2 = 0;
					}
				} else {
					_margin = _margin + _step;
					if (_margin == _liSum - _gWidth - _options.innerMargin) {
						jQuery(_options.btNext,_this).addClass('next-'+_options.disableClass);_f2 = 0;
					}
				}
			} else {
				if (_margin + _step  > _liSum - _gWidth + _options.innerMargin) {
					if (_margin != _liSum - _gWidth + _options.innerMargin) {

						_margin = _liSum - _gWidth  + _options.innerMargin;
					} else {
						_f2 = 1;
						_margin = -_options.innerMargin;

					}
				} else {
					_margin = _margin + _step;
					_f2 = 0;
				}
			}

			_animatedBlock.animate({marginLeft: -_margin+"px"}, {queue:false,duration: _options.duration });

			if (_timerSlide) {
				clearTimeout(_timerSlide);
				_timerSlide = setTimeout(function(){
					autoSlide(_options.autoSlide)
				}, _options.autoSlide);
			}

			if (_options.slideNum && !_options.step) jQuery.fn.galleryScroll.numListActive(_margin,jQuery(_options.slideNum, _this),_gWidth,_lastSection);
			if (jQuery.isFunction(_options.funcOnclick)) {
				_options.funcOnclick.apply(_this);
			}
			e.preventDefault();
		});
		var _f2 = 1;
		jQuery(_options.btPrev, _this).bind('click',function(e){
			jQuery(_options.btNext,_this).removeClass('next-'+_options.disableClass);
			if (_margin - _step >= -_step - _options.innerMargin && _margin - _step <= -_options.innerMargin) {
				if (_f2 != 1) {
					_margin = -_options.innerMargin;
					_f2 = 1;
				} else {
					if (_options.circleSlide) {
						_margin = _liSum - _gWidth  + _options.innerMargin;
						f=1;_f2=0;
					} else {
						_margin = -_options.innerMargin
					}
				}
			} else if (_margin - _step < -_step + _options.innerMargin) {
				_margin = _margin - _step;
				f=0;
			}
			else {_margin = _margin - _step;f=0;};

			if (!_options.circleSlide && _margin == _options.innerMargin) {
				jQuery(this).addClass('prev-'+_options.disableClass);
				_f2=0;
			}

			if (!_options.circleSlide && _margin == -_options.innerMargin) jQuery(this).addClass('prev-'+_options.disableClass);
			_animatedBlock.animate({marginLeft: -_margin + "px"}, {queue:false, duration: _options.duration});

			if (_options.slideNum && !_options.step) jQuery.fn.galleryScroll.numListActive(_margin,jQuery(_options.slideNum, _this),_gWidth,_lastSection);

			if (_timerSlide) {
				clearTimeout(_timerSlide);
				_timerSlide = setTimeout(function(){
					autoSlide(_options.autoSlide)
				}, _options.autoSlide);
			}

			if (jQuery.isFunction(_options.funcOnclick)) {
				_options.funcOnclick.apply(_this);
			}
			e.preventDefault();
		});

		if (_liSum <= _gWidth) {
			jQuery(_options.btPrev,_this).addClass('prev-'+_options.disableClass).unbind('click');
			jQuery(_options.btNext,_this).addClass('next-'+_options.disableClass).unbind('click');
		}
		// auto slide
		function autoSlide(autoSlideDuration){
			//if (_options.circleSlide) {
				jQuery(_options.btNext,_this).trigger('click');
			//}
		};
		// Number list
		jQuery.fn.galleryScroll.numListCreate = function(_elNumList, _liSumWidth, _width, _section){
			var _numListElC = '';
			var _num = 1;
			var _difference = _liSumWidth + _section;
			while(_difference > 0)
			{
				_numListElC += '<li><a href="">'+_num+'</a></li>';
				_num++;
				_difference = _difference - _width;
			}
			jQuery(_elNumList).html(_numListElC);
		};
		jQuery.fn.galleryScroll.numListActive = function(_marginEl, _slideNum, _width, _section){
			if (_slideNum) {
				jQuery('a',_slideNum).removeClass('active');
				var _activeRange = _width - _section-1;
				var _n = 0;
				if (_marginEl != 0) {
					while (_marginEl > _activeRange) {
						_activeRange = (_n * _width) -_section-1 + _options.innerMargin;
						_n++;
					}
				}
				var _a  = (_activeRange+_section+1 + _options.innerMargin)/_width - 1;
				jQuery('a',_slideNum).eq(_a).addClass('active');
			}
		};
		if (_options.slideNum && !_options.step) {

			jQuery.fn.galleryScroll.numListCreate(jQuery(_options.slideNum, _this), _liSum, _gWidth,_lastSection);
			jQuery.fn.galleryScroll.numListActive(_margin, jQuery(_options.slideNum, _this),_gWidth,_lastSection);
			numClick();
		};
		function numClick() {
			jQuery(_options.slideNum, _this).find('a').click(function(e){
				jQuery(_options.btPrev,_this).removeClass('prev-'+_options.disableClass);
				jQuery(_options.btNext,_this).removeClass('next-'+_options.disableClass);

				var _indexNum = jQuery(_options.slideNum, _this).find('a').index(jQuery(this));
				_margin = (_step*_indexNum) - _options.innerMargin;
				f=0; _f2=0;
				if (_indexNum == 0) _f2=1;
				if (_margin + _step > _liSum) {
					_margin = _margin - (_margin - _liSum) - _step + _options.innerMargin;
					if (!_options.circleSlide) jQuery(_options.btNext, _this).addClass('next-'+_options.disableClass);
				}
				_animatedBlock.animate({marginLeft: -_margin + "px"}, {queue:false, duration: _options.duration});

				if (!_options.circleSlide && _margin==0) jQuery(_options.btPrev,_this).addClass('prev-'+_options.disableClass);
				jQuery.fn.galleryScroll.numListActive(_margin, jQuery(_options.slideNum, _this),_gWidth,_lastSection);

				if (_timerSlide) {
					clearTimeout(_timerSlide);
					_timerSlide = setTimeout(function(){
						autoSlide(_options.autoSlide)
					}, _options.autoSlide);
				}
				e.preventDefault();
			});
		};
		jQuery(window).resize(function(){
			_gWidth = _holderBlock.width();
			_liWidth = jQuery(_options.scrollEl,_animatedBlock).outerWidth(true);
			_liSum = jQuery(_options.scrollEl,_animatedBlock).length * _liWidth;
			if (!_options.step) _step = _gWidth; else _step = _options.step*_liWidth;
			if (_options.slideNum && !_options.step) {
				var _lastSection = 0;
				var _sectionWidth = 0;
				while(_sectionWidth < _liSum)
				{
					_sectionWidth = _sectionWidth + _gWidth;
					if(_sectionWidth > _liSum) {
					       _lastSection = _sectionWidth - _liSum;
					}
				};
				_animatedBlock.css('margin-left',-(_liWidth*_holderBlock.find('.switcher .active').parent().index()));
			};
		});
	});
}
$.fn.popup = function(o){
	var o = $.extend({
				"opener":".call-back a",
				"popup_holder":"#call-popup",
				"popup":".popup",
				"close_btn":".close",
				"close":function(){},
				"beforeOpen":function(popup_holder){$(popup_holder).css('left',0).hide()}
			},o);
	return this.each(function(){
		var container=$(this),
			opener=$(o.opener,container),
			popup_holder=$(o.popup_holder,container),
			popup=$(o.popup,popup_holder),
			close=$(o.close_btn,popup),
			bg=$('.bg',popup_holder);
			popup.css('margin',0);
			opener.click(function(e){
				o.beforeOpen.apply(this,[popup_holder]);
				popup_holder.fadeIn(400);
				alignPopup();
				bgResize();
				e.preventDefault();
				$('.popup-holder').each(function(){
					if ($(this).offset().left == 0){
						$(this).find('input:first').focus();
					};
				});
			});
		function alignPopup(){
				if((($(window).height() / 2) - (popup.outerHeight() / 2))+ $(window).scrollTop()<0){
					popup.css({'top':0,'left': (($(window).width() - popup.outerWidth())/2) + $(window).scrollLeft()});
					return false;
				}
				popup.css({
					'top': (($(window).height()-popup.outerHeight())/2) + $(window).scrollTop(),
					'left': (($(window).width() - popup.outerWidth())/2) + $(window).scrollLeft()
				});
		}
		function bgResize(){
			var _w=$(window).width(),
				_h=$(document).height();
			bg.css({"height":_h,"width":_w+$(window).scrollLeft()});
		}
		$(window).resize(function(){
			if(popup_holder.is(":visible")){
				bgResize();
				alignPopup();
			}
		});
		if(popup_holder.is(":visible")){
				bgResize();
				alignPopup();
		}
		close.add(bg).click(function(e){
			var closeEl=this;
			popup_holder.fadeOut(400,function(){
				o.close.apply(closeEl,[popup_holder]);
			});
			e.preventDefault();
		});
		$('body').keydown(function(e){
			if(e.keyCode=='27'){
				popup_holder.fadeOut(400);
			}
		})
	});
}