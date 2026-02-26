gsap.registerPlugin(ScrollTrigger, SplitText);
gsap.config({
	nullTargetWarn: false,
	trialWarn: false
});

/*----  Functions  ----*/
function pbmit_img_animation() {
	const boxes = gsap.utils.toArray('.pbmit-animation-style1,.pbmit-animation-style2,.pbmit-animation-style3,.pbmit-animation-style4,.pbmit-animation-style5,.pbmit-animation-style6');
	boxes.forEach(img => {
		gsap.to(img, {
			scrollTrigger: {
				trigger: img,
				start: "top 70%",
				end: "bottom bottom",
				toggleClass: "active",
				once: true,
			}
		});
	});
}

// ** Hover Image Effect ** \\
function pbmit_hover_img() {
	const pbmitHoverImg = gsap.utils.toArray(".pbmit-ihbox-style-2,.pbmit-timeline .pbmit-content, .pbmit-team-style-2 .pbminfotech-box-content-inner,.pbmit-element-service-style-9 article");
	pbmitHoverImg.forEach((target) => {
		const pbmitImg = target.querySelector('.pbmit-hover-img');
		const t1 = gsap.timeline();
		t1.to(pbmitImg, {
			opacity: 1,
			duration: 0.4,
			scale: 1,
			ease: "Power2.easeOut"
		})
		target.pbmitHoverAnim = t1.play().reversed(true);
		target.addEventListener("mouseenter", pbmithoverimg);
		target.addEventListener("mouseleave", pbmithoverimg);
		target.addEventListener("mousemove", (e) => {
			let xpos = e.offsetX;
			let ypos = e.offsetY;
			const t1 = gsap.timeline();
			t1.to(pbmitImg, { x: xpos, y: ypos });
		});
	});

	function pbmithoverimg() {
		this.pbmitHoverAnim.reversed(!this.pbmitHoverAnim.reversed());
	}
}

function getpercentage(x, y, elm) {
	elm.find('.pbmit-fid-inner').html(y + '/' + x);
	var cal = Math.round((y * 100) / x);
	return cal;
}

function pbmit_staticbox_hover() {
	var pbmit_var = $('.pbmit-element-static-box-style-1, .pbmit-element-static-box-style-2, .pbmit-element-award-box-style-1, .pbmit-element-portfolio-style-9');
	if (!pbmit_var.length) {
		return;
	}
	pbmit_var.each(function() {
		var pbmit_Class = '.pbmit-element-posts-wrapper > .pbmit-ele-static-box,.pbmit-award-box-wraper';
		$(this)
			.find(pbmit_Class).first()
			.addClass('pbmit-active');
		$(this)
			.find(pbmit_Class)
			.on('mouseover', function() {
				$(this).addClass('pbmit-active').siblings().removeClass('pbmit-active');
			});
	});
}

function pbmit_title_animation() {

	var pbmit_var = $('.pbmit-heading-subheading');
	if (!pbmit_var.length) {
		return;
	}
	const quotes = document.querySelectorAll(".pbmit-heading-subheading .pbmit-element-title, .pbmit-custom-heading .pbmit-element-title ");

	quotes.forEach(quote => {

		//Reset if needed
		if (quote.animation) {
			quote.animation.progress(1).kill();
			quote.split.revert();
		}

		var getclass = quote.closest('.pbmit-heading-subheading, .pbmit-custom-heading').className;
		var animation = getclass.split('animation-');
		if (animation[1] == "style4") return

		quote.split = new SplitText(quote, {
			type: "lines,words,chars",
			linesClass: "split-line"
		});
		gsap.set(quote, { perspective: 400 });

		if (animation[1] == "style1") {
			gsap.set(quote.split.chars, {
				opacity: 0,
				y: "90%",
				rotateX: "-40deg"
			});
		}
		if (animation[1] == "style2") {
			gsap.set(quote.split.chars, {
				opacity: 0,
				x: "50"
			});
		}
		if (animation[1] == "style3") {
			gsap.set(quote.split.chars, {
				opacity: 0,
			});
		}
		quote.animation = gsap.to(quote.split.chars, {
			scrollTrigger: {
				trigger: quote,
				start: "top 90%",
			},
			x: "0",
			y: "0",
			rotateX: "0",
			opacity: 1,
			duration: 1,
			ease: Back.easeOut,
			stagger: .02
		});
	});
}

function pbmit_special_heading(){
	var pbmit_var = $('.pbmit-special-heading');
	if (!pbmit_var.length) {
		return;
	}
	pbmit_var.addClass('active'); 
	const splitText = new SplitText(".pbmit-special-heading h1").chars;
	const timeline = gsap.timeline({defaults:{duration:0.6, stagger:{amount:0.3, ease:'sine.in'},delay: 1}})
	.from(splitText, {
		opacity: 0,
		y: "90%",
		rotateX: "-40deg",
		
	}, 0)
	.to(splitText, {
		opacity: 1,
		y: "0%",
		rotateX: "0deg",
		transformOrigin: "50% 50%",
		
	}, 0)
		
}

function pbmit_sticky() {

	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {

			let pbmit_sticky_container = $(".pbmit-sticky-col");

			let section = pbmit_sticky_container.closest('section');
			if (!section[0]) {
				section = pbmit_sticky_container.closest('.pbmit-sticky-section');
			}

			let tl = gsap.timeline({
				scrollTrigger: {
					pin: true,
					scrub: 1,
					trigger: pbmit_sticky_container,
					end: () => "+=" + ((section.height() + 200) - document.documentElement.clientHeight)
				},
				defaults: { ease: "none", duration: 1 }
			});
		},
	});
}

function pbmit_sticky_menu() {
	if (!$(".pbmit-element-split-slide-style-1,.pbmit-element-split-slide-style-2,.pbmit-element-award-box-style-1, .pbmit-element-split-slide-style-3")[0]) {
		return
	}
	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {

			let container = $(".pbmit-element-split-slide-style-1 .pbmit-img,.pbmit-element-split-slide-style-2 .pbmit-img,.pbmit-element-award-box-style-1 .pbmit-img, .pbmit-element-split-slide-style-3 .pbmit-img");
			let section = $(".pbmit-element-split-slide-style-1 .pbmit-element-split-slide-wrapper,.pbmit-element-split-slide-style-2 .pbmit-element-split-slide-wrapper,.pbmit-element-award-box-style-1 .pbmit-element-award-box-wrapper, .pbmit-element-split-slide-style-3 .pbmit-element-split-slide-wrapper");
			var indicators = gsap.utils.toArray('.pbmit-element-split-slide-style-1 .pbmit-split-slide-item-image, .pbmit-element-split-slide-style-2 .pbmit-split-slide-item-image,.pbmit-element-award-box-style-1 .pbmit-award-item-image, .pbmit-element-split-slide-style-3 .pbmit-split-slide-item-image');
			var points = gsap.utils.toArray('.pbmit-element-split-slide-style-1 .pbmit-bg-imgbox .pbmit-split-slide-box,.pbmit-element-split-slide-style-2 .pbmit-bg-imgbox .pbmit-split-slide-box,.pbmit-element-award-box-style-1 .pbmit-bg-imgbox .pbmit-menu-box, .pbmit-element-split-slide-style-3 .pbmit-bg-imgbox .pbmit-split-slide-box');

			var gap = points.length * 5;

			let tl = gsap.timeline({
				scrollTrigger: {
					pin: true,
					scrub: 1,
					trigger: container,
					end: () => "+=" + ((section.height() + gap) - document.documentElement.clientHeight),
					onUpdate: (self) => {
						let per = parseInt(self.progress * 100);
						if (per > 99) indicators[points.length - 1].classList.add('last');
						else indicators[points.length - 1].classList.remove('last');
						if (per < 1) indicators[0].classList.add('first');
						else indicators[0].classList.remove('first');

					}
				},
				defaults: { ease: "none", duration: 1 }
			});

			points.forEach((sct, i) => {
				let pos = indicators[i];
				ScrollTrigger.create({
					trigger: sct,
					start: "top center",
					end: () => '+=' + sct.offsetHeight,
					toggleClass: { targets: pos, className: "active" }
				});
			});
			$('.pbmit-element-split-slide-style-1 .pbmit-bg-imgbox .pin-spacer .pbmit-split-slide-item-image:first-child,.pbmit-element-split-slide-style-2 .pbmit-bg-imgbox .pin-spacer .pbmit-split-slide-item-image:first-child,.pbmit-element-award-box-style-1 .pbmit-bg-imgbox .pin-spacer .pbmit-award-item-image:first-child, .pbmit-element-split-slide-style-3 .pbmit-bg-imgbox .pin-spacer .pbmit-split-slide-item-image:first-child').addClass('active');
		},
		"(max-width:992px)": function() {
			ScrollTrigger.getAll().forEach(pin => pin.kill(true));
		}
	});

}
function pbmit_dot_masking() {
	if (!$(".pbmit-dot-mask")[0]) {
		return
	}
	ScrollTrigger.matchMedia({
		"(min-width: 991px)": function() {
	
			$('.pbmit-dot-mask').append("<div class='pbmit-dot-masking'></div>");
			let tl = gsap.timeline({
				scrollTrigger: {
					trigger: ".pbmit-dot-mask",
					start: "top 1%",
					pin: true,
					end: () => '+=' + 1000,
					scrub: 1, 
					onUpdate: (timeline)=>{
						let per = Math.round(timeline.progress * 100);
						if(per > 90){
							$('.pbmit-dot-masking').addClass('active');
						}else{
							$('.pbmit-dot-masking').removeClass('active');
						}
					},
				},
				defaults: { ease: "none" }
			});
			tl.to('.pbmit-dot-masking', { width: 3000, height: 3000})
		},
		"(max-width:992px)": function() {
			ScrollTrigger.getAll().forEach(tl => tl.kill(true));
		}
	});
}
function pbmit_dot_masking2() {
	let pbmit_dot_wrap = ".pbmit-dot-mask2";
	if (!jQuery(pbmit_dot_wrap)[0]) {
		return
	} 
	ScrollTrigger.matchMedia({
		"(min-width: 1201px)": function() {
			let pbmit_dot = ".pbmit-dot-masking2";
			jQuery(pbmit_dot_wrap).append("<div class='pbmit-dot-masking2'></div>");
			
			let tl = gsap.timeline({
				scrollTrigger: {
					trigger: ".pbmit-dot-masking2-start",
					start: "top 70%", 
					end: "bottom 50%", 
					scrub: 1,
					onUpdate: (timeline)=>{
						let per = Math.round(timeline.progress * 100);
						if(per > 10){
							jQuery(pbmit_dot).removeClass('active');
						}
					},
					defaults: { ease: "none", duration: 1 }
				}
			});
			let t2 = gsap.timeline({
				scrollTrigger: {
					trigger: ".pbmit-dot-masking2-end",
					start: "top 10%", 
					end: "bottom bottom", 
					scrub: 1, 					   
					onUpdate: (timeline)=>{
						let per = Math.round(timeline.progress * 100);
						if(per > 10){
							jQuery(pbmit_dot).addClass('active');
						}
					}, 
					defaults: { ease: "none", duration: 1 }
				}
			});
			
			tl.to(pbmit_dot, { scale: 40}) 
			t2.to(pbmit_dot, { scale: 0})
		},
		"(max-width:1201px)": function() {
			ScrollTrigger.getAll().forEach(tl => tl.kill(true));
		}
	});
}
function pbmit_dot_masking2_add_class() {

	const $startTriggers = gsap.utils.toArray(".pbmit-dot-mask2");
	if (!$startTriggers[0]) {
		return
	}
	ScrollTrigger.matchMedia({
		"(min-width: 1201px)": function() {
			$startTriggers.forEach(elm => {
				let $startTrigger = jQuery(elm);
				const color = $startTrigger.css("background-color");
				$startTrigger.css("background-color", "transparent");

				ScrollTrigger.create({
					trigger: $startTrigger,
					start: "top 40%",
					end: "bottom bottom",
					onEnter: () => {						
						$startTrigger.addClass("pbmit-text-color-white");
					},
					onEnterBack: () => {						
						$startTrigger.addClass("pbmit-text-color-white");
					},
					onLeaveBack: () => {
						$startTrigger.removeClass("pbmit-text-color-white");
					},
					onLeave: () => {						
						$startTrigger.removeClass("pbmit-text-color-white");
					}
				});
			});
		},
		"(max-width:1201px)": function() {
			ScrollTrigger.getAll().forEach($ScrollTrigger => $ScrollTrigger.kill(true));
		}
	});
}
function pbmit_reel_video() {
	if (!$(".pbmit-element-reel-video-style-1,.pbmit-element-reel-video-style-2")[0]) {
		return
	} 
	ScrollTrigger.matchMedia({
		"(min-width: 991px)": function() {

			let tl = gsap.timeline({
				scrollTrigger: {
					trigger: ".pbmit-element-reel-video-style-1,.pbmit-element-reel-video-style-2",
					start: "top 1%",
					pin: true,
					end: () => '+=' + 1000,
					scrub: 1 
				},
				defaults: { ease: "none" }
			}); 
			tl.set('.pbmit-reel-t1', { x: -450})
			tl.set('.pbmit-reel-t2', { x: 450})
			tl.to('.pbmit-video-wrapper iframe', { scale: 1},0)	
			tl.to('.pbmit-reel-t1', { x: 0},0)
			tl.to('.pbmit-reel-t2', { x: 20},0)
		},
		"(max-width:992px)": function() {
			ScrollTrigger.getAll().forEach(tl => tl.kill(true));
		}
	});
}
function pbmit_gallery() {

	if (!$(".pbmit-gallery-style-1")[0]) {
		return
	} 
	ScrollTrigger.matchMedia({
		"(min-width:992px)": function() {
			const items = document.querySelectorAll('.pbmit-gallery-style-1');
			const columnWraps = document.querySelectorAll('.pbmit-element-gallery-style-1 .pbmit-column');
			gsap.timeline({
				scrollTrigger: {
					start: 0,
					end: 'max',
					scrub: true
				}
			})
			.addLabel('start', 0)
			.to(items, {
				scrollTrigger: {
					trigger:'.pbmit-element-gallery-style-1',
					start: 'top 100%',
					end: "bottom 20%",
					scrub: true
				},
				ease: 'power4.inOut',
				startAt: {
					opacity: 0.2,
					filter: 'brightness(100%)'
				},
				opacity: 1,
				filter: 'brightness(100%)', 
				yoyo: true,
				repeat: 1
			}, 'start')
			.to(columnWraps, {
				ease: 'none',
				yPercent: pos => pos*-20-20
			}, 'start')
		},
	});	
}

function pbmit_action_box() {
	const pbmit_elm = gsap.utils.toArray('.pbmit-action-box');
	if (pbmit_elm.length == 0) return
	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {
			pbmit_elm.forEach((box, i) => {
				let tl = gsap.timeline({
					scrollTrigger: {
						trigger: box,
						pin: true,
						start: "top top",
						end: "+=700px",
						scrub: 1
					},
					defaults: { ease: "none" }
				});
				tl.fromTo(box.querySelector(".pbmit-action-box-circle-wrap"), { clipPath: 'circle(15% at 50% 50%)' }, { clipPath: 'circle(100% at 50% 50%)', duration: 3 })
				tl.fromTo(box.querySelector(".pbmit-action-box-wrap"), { clipPath: 'inset(10% 20% 20% 20%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 3 })
				tl.fromTo(box.querySelector(".pbmit-action-content"), { opacity: 0, y: "70%", }, { opacity: 1, y: 0, duration: 1.5 })
				tl.fromTo(box.querySelector(".pbmit-action-content"), { opacity: 1 }, { opacity: 1, duration: 5 })
			});
		}
	});
}
function pbmit_portfolio_style2() {
	if (typeof Swiper !== 'undefined') {
		const pbmit_elm = gsap.utils.toArray('.pbmit-element-portfolio-style-2');
		if (pbmit_elm.length == 0) return 

		ScrollTrigger.matchMedia({
			"(min-width:768px)": function() {

				var thisAnimWrap = document.querySelector('.pbmit-element-portfolio-style-2 .pbmit-element-posts-wrapper');	
				var getToValue = -(thisAnimWrap.scrollWidth - window.innerWidth) - 100; 
		
				gsap.to(thisAnimWrap, {
					x: () => getToValue,
					ease: "none",
					scrollTrigger: {
						trigger: pbmit_elm,  
						start: "top top",
						end: () => "+=" + (thisAnimWrap.scrollWidth - window.innerWidth),
						pin: pbmit_elm, 
						scrub: 1, 
						markers: false,
						invalidateOnRefresh: true
					},
				}); 
			},
			"(max-width:768px)": function() {
				ScrollTrigger.getAll().forEach(pin => pin.kill(true));
			}
		});
	}
}
function pbmit_portfolio_style3() {
	ScrollTrigger.matchMedia({
		"(min-width:992px)": function() {
			if (typeof Swiper !== 'undefined') {
				const pbmit_elm = gsap.utils.toArray('.pbmit-element-portfolio-style-3');
				if (pbmit_elm.length == 0) return 
				var total = $('.pbmit-element-portfolio-style-3 .pbminfotech-post-content').length;	
				$('.pbmit-element-portfolio-style-3 .pbmit-element-inner').append('<div class="project-number-slider">0<span class="current-number">1</span><span>0' + total + '</span></div>');
				var thisAnimWrap = document.querySelector('.pbmit-element-portfolio-style-3 .pbmit-element-posts-wrapper');	
				var getToValue = -(thisAnimWrap.scrollWidth - window.innerWidth) - 100;  
				let scrollTween = gsap.to(thisAnimWrap, {
					x: () => getToValue,
					ease: "none",
					scrollTrigger: {
						trigger: pbmit_elm,  
						start: "top top",
						end: () => "+=" + (thisAnimWrap.scrollWidth - window.innerWidth),
						pin: pbmit_elm, 
						scrub: 1, 
						markers: false,
						invalidateOnRefresh: true,
						onUpdate: (self) => { 				 
								var index = $('.pbmit-element-portfolio-style-3 .pbminfotech-post-content.active').index();	  
								if (index >= 0) { 
									$('.pbmit-element-portfolio-style-3 .current-number').html(index + 1);
								}
							} 
					},
				});  
				
				const pbmproject = document.querySelectorAll('.pbmit-element-portfolio-style-3 .pbminfotech-post-content');
				pbmproject.forEach((section, index) => {
					gsap.to(section, {
						scale: 0.7, 
						ease: "none",
						scrollTrigger: {
						trigger: section,
						containerAnimation: scrollTween,
						start: "right 100%",
						end: "right 80%",
						scrub: true,
						toggleClass: { targets: section, className: "active" }
						}
					});  
				});
			}
		}
	});
}
function pbmit_portfolio_style5() { 
	var myswiper; 

			if (typeof Swiper !== 'undefined') {
				myswiper = new Swiper(".pbmit-element-portfolio-style-5 .swiper-container", {
					direction: "vertical",
					effect: 'crative',
					mousewheel: true,
					slidesPerView: 1,
					spaceBetween: 0,
					speed: 800,
					mousewheel: {
						enabled: false,
					},
					pagination: {
						el: '.pbmit-element-portfolio-style-5 .swiper-pagination',
						clickable: true,
						renderBullet: function (index, className) {
						  return '<span class="' + className + '">' + ('0' + (index + 1)) + '</span>';
						},
					  },

					on: {
						slideChange: function() {
							setTimeout(function () {
								myswiper.params.mousewheel.releaseOnEdges = false;
							}, 500);
						},
						reachEnd: function() {
							setTimeout(function () {
								myswiper.params.mousewheel.releaseOnEdges = true;
							}, 750);
						},
						reachBeginning: function() {
							setTimeout(function () {
								myswiper.params.mousewheel.releaseOnEdges = true;
							}, 750);
						}
					},	
					breakpoints:{
						768: {
							mousewheel: {
								enabled: true,
							},
							pagination: {
								clickable: true,
							}
						},
					}				
				});				
			}		
		 
}
function pbmit_portfolio_style8() {
	var elm = $('.pbmit-portfolio-style-8');
	if (!elm.length) {
		return;
	} 
	var bg_area = elm.closest('.personal-port-2-portfolio');	
	gsap.to(bg_area, {
		backgroundColor: elm.first().find('.pbminfotech-post-content').data("bgcolor")
	})
	elm.hover(function () {
			var bg_color = $(this).find('.pbminfotech-post-content').data("bgcolor");
			gsap.to(bg_area, {
				backgroundColor: bg_color
			})
		}
	 );
}

function pbmit_verticle_slide_image() {

	ScrollTrigger.matchMedia({
		"(min-width:768px)": function() {

			const pbmitvar = document.querySelectorAll('.pbmit-vertical-box-style-1');
			let totalheight = -300;
			pbmitvar.forEach((section, index) => {
				totalheight += section.offsetHeight;
				gsap.to(section, {
					yPercent: -50,
					scrollTrigger: {
						trigger: section,
						scrub: 3
					}
				});
			});

			ScrollTrigger.create({
				trigger: ".pbmit-element-vertical-box-style-1 ",
				pin: '.pbmit-element-vertical-box-style-1 .pbmit-heading-subheading ',
				start: () => "top top",
				end: () => "+=" + totalheight,
				invalidateOnRefresh: false,
			});
		}
	});
}


function pbmit_set_tooltip() {
	$('[data-cursor-tooltip]').each(function() {
		var thisele = $(this);
		var thisele_html = thisele.find('.pbminfotech-box-content').html();
		thisele.attr("data-cursor-tooltip", thisele_html);
	});
}

function pbmit_tween_effect() {

	const pbmit_tween = gsap.utils.toArray('.pbmit-tween-effect');
	if (pbmit_tween.length == 0) return

	ScrollTrigger.matchMedia({
		"(min-width: 767px)": function() {

			pbmit_tween.forEach((box, i) => {
				let tl = gsap.timeline({
					scrollTrigger: {
						trigger: box,
						start: "top 90%",
						end: "bottom 70%",
						scrub: 1
					},
					defaults: { ease: "none" }
				});

				let xpos_val = box.getAttribute('data-x-start');
				let xpose_val = box.getAttribute('data-x-end');
				let ypos_val = box.getAttribute('data-y-start');
				let ypose_val = box.getAttribute('data-y-end');

				let scale_x_val = box.getAttribute('data-scale-x-start');
				let scale_xe_val = box.getAttribute('data-scale-x-end');

				let skew_x_val = box.getAttribute('data-skew-x-start');
				let skew_xe_val = box.getAttribute('data-skew-x-end');
				let skew_y_val = box.getAttribute('data-skew-y-start');
				let skew_ey_val = box.getAttribute('data-skew-y-end');

				let rotation_x_val = box.getAttribute('data-rotate-x-start');
				let rotation_xe_val = box.getAttribute('data-rotate-x-end');
				gsap.set(box, { xPercent: xpos_val, yPercent: ypos_val, scale: scale_x_val, skewX: skew_x_val, skewY: skew_y_val, rotation: rotation_x_val });
				tl.to(box, { xPercent: xpose_val, yPercent: ypose_val, scale: scale_xe_val, skewX: skew_xe_val, skewY: skew_ey_val, rotation: rotation_xe_val })
			});
		},
	});
}
function pbmit_portfolio_effect() {
	const images = gsap.utils.toArray('.pbmit-portfolio-style-6,.pbmit-portfolio-style-12');
	if (images.length == 0) return
	const images_inner = gsap.utils.toArray('.pbmit-portfolio-style-6 .pbmit-featured-wrapper,.pbmit-portfolio-style-12 .pbmit-featured-wrapper	');
	images.forEach(img => {
		gsap.to(img, {
			scrollTrigger: {
				trigger: img,
				start: "top 70%",
				end: "bottom bottom",
				toggleClass: "active",
				once: true,
			}
		});
	});
	images_inner.forEach(img => {
		let tl = gsap.timeline({
			scrollTrigger: {
				trigger: img,
				start: "top 20%",
				end: "bottom bottom",
				scrub: 3
			},
		});
		tl.fromTo(img, { y: 0 }, { y: 40 })
	});
}

// ** Text Mask Animation ** \\

function pbmit_team_mask_animation() {
	$(".pbmit-element-team-style-2").append("<div class='pbmit-team-cursor-mask'><div class='pbmit-team-cursor'></div></div>");
	const pbmit_class = document.querySelector('.pbmit-element-team-style-2');

	var pbmit_var = $('.pbmit-element-team-style-2');
	if (!pbmit_var.length) {
		return;
	}
	const el = document.querySelector('.pbmit-team-cursor');
	pbmit_class.addEventListener('mousemove', (e) => {
		el.classList.add("active");
		let offsetLeft = pbmit_class.offsetLeft || pbmit_class.getBoundingClientRect().left;
		let offsetTop = pbmit_class.offsetTop || pbmit_class.getBoundingClientRect().top;
		const x1 = e.clientX - offsetLeft;
		const y1 = e.clientY - offsetTop;

		gsap.to(el, {
			x: x1,
			y: y1,
			duration: 0.3,
			ease: 'sine.out',
		})
	})
	pbmit_class.addEventListener('mouseleave', (e) => {
		el.classList.remove("active");
	})
}

function pbmit_button_hover() {
  const all_btns = gsap.utils.toArray(".pbmit-btn-style-text.pbmit-btn-shape-outline .elementor-button-wrapper,.pbmit-btn-style-text.pbmit-btn-shape-outline .pbmit-button-wrapper");
  if (all_btns.length > 0) {
	var all_btn = gsap.utils.toArray(".pbmit-btn-style-text.pbmit-btn-shape-outline .elementor-button-wrapper,.pbmit-btn-style-text.pbmit-btn-shape-outline .pbmit-button-wrapper");
  }
  else {
	var all_btn = gsap.utils.toArray("#elementor-button-wrapper");
  }
  const all_btn_cirlce = gsap.utils.toArray(".pbmit-btn-style-text.pbmit-btn-shape-outline .elementor-button, .pbmit-btn-style-text.pbmit-btn-shape-outline .pbmit-button");
  all_btn.forEach((btn, i) => {
	$(btn).mousemove(function (e) {
	  callParallax(e);
	});
	function callParallax(e) {
	  parallaxIt(e, all_btn_cirlce[i], 10);
	}

	function parallaxIt(e, target, movement) {
	  var $this = $(btn);
	  var relX = e.pageX - $this.offset().left;
	  var relY = e.pageY - $this.offset().top;

	  gsap.to(target, 0.5, {
		x: ((relX - $this.width() / 2) / $this.width()) * movement,
		y: ((relY - $this.height() / 2) / $this.height()) * movement,
		ease: Power2.easeOut,
	  });
	}
	$(btn).mouseleave(function (e) {
	  gsap.to(all_btn_cirlce[i], 0.5, {
		x: 0,
		y: 0,
		ease: Power2.easeOut,
	  });
	});
  });
}

function pbmit_button_hover_move() {
 $('.pbmit-outline-btn').on('mouseenter', function (e) {
	var x = e.pageX - $(this).offset().left;
	var y = e.pageY - $(this).offset().top;

	$(this).find('.pbmit-button-hover').css({
	  top: y,
	  left: x
	});
  });

  $('.pbmit-outline-btn').on('mouseout', function (e) {
	var x = e.pageX - $(this).offset().left;
	var y = e.pageY - $(this).offset().top;

	$(this).find('.pbmit-button-hover').css({
	  top: y,
	  left: x
	});
  });
}

function pbmit_vertical_style() {
	var pbmit_var = $('.pbmit-element-portfolio-style-10');
	if (!pbmit_var.length) {
		return;
	}
	 /*--------------------
	Vars
	--------------------*/
	const $menu = document.querySelector('.pbmit-element-portfolio-style-10 .pbmit-element-posts-wrapper')
	const $items = document.querySelectorAll('.pbmit-element-portfolio-style-10 .pbmit-portfolio-style-10')
	const $items_title = document.querySelectorAll('.pbmit-element-portfolio-style-10 .pbmit-image-wrapper')
	let menuHeight = $menu.clientHeight
	let itemHeight = $items[0].clientHeight
	let wrapHeight = $items.length * itemHeight 
	let scrollSpeed = 0
	let oldScrollY = 0
	let scrollY = 0
	let y = 0
	/*--------------------
	Lerp
	--------------------*/
	const lerp = (v0, v1, t) => {
		return v0 * ( 1 - t ) + v1 * t
	}
	/*--------------------
	Dispose
	--------------------*/
	const dispose = (scroll) => {
		gsap.set($items, {
			y: (i) => {
			return i * itemHeight + scroll
			},
			modifiers: {
			y: (y) => {
				const s = gsap.utils.wrap(-itemHeight, wrapHeight - itemHeight, parseInt(y))			 
				return `${s}px`
			}
			}
		})
	} 
	dispose(0)
	/*--------------------
	Wheel
	--------------------*/
	const handleMouseWheel = (e) => {
		scrollY -= e.deltaY  
	}

	/*--------------------
	Touch
	--------------------*/
	let touchStart = 0
	let touchY = 0
	let isDragging = false
	const handleTouchStart = (e) => {
		touchStart = e.clientY || e.touches[0].clientY
		isDragging = true
		$menu.classList.add('is-dragging')
	}
	const handleTouchMove = (e) => {
	if (!isDragging) return
		touchY = e.clientY || e.touches[0].clientY
		scrollY += (touchY - touchStart) * 2.5
		touchStart = touchY
	}
	const handleTouchEnd = () => {
		isDragging = false
		$menu.classList.remove('is-dragging')
	}
	/*--------------------
	Listeners
	--------------------*/
	$menu.addEventListener('mousewheel', handleMouseWheel)

	$menu.addEventListener('touchstart', handleTouchStart)
	$menu.addEventListener('touchmove', handleTouchMove)
	$menu.addEventListener('touchend', handleTouchEnd)

	$menu.addEventListener('mousedown', handleTouchStart)
	$menu.addEventListener('mousemove', handleTouchMove)
	$menu.addEventListener('mouseleave', handleTouchEnd)
	$menu.addEventListener('mouseup', handleTouchEnd)

	$menu.addEventListener('selectstart', () => { return false })

	/*--------------------
	Resize
	--------------------*/
	window.addEventListener('resize', () => {
		menuHeight = $menu.clientHeight
		itemHeight = $items[0].clientHeight
		wrapHeight = $items.length * itemHeight
	})


	/*--------------------
	Render
	--------------------*/
	const render = () => {
	requestAnimationFrame(render)
	y = lerp(y, scrollY, .1)
	dispose(y)
 
	scrollSpeed = y - oldScrollY
	oldScrollY = y 
	gsap.to($items_title, {
		skewY: -scrollSpeed * .2,
		rotate: scrollSpeed * .01,
		scale: 1 - Math.min(100, Math.abs(scrollSpeed)) * 0.003
	 })
	}
	render()
}

function pbmit_service_style4(){
	var pbmit_var = $('.pbmit-service-style-4');
	if (!pbmit_var.length) {
		return;
	}
	pbmit_var.each(function( index ) {
		var f_letter = $(this).find('.pbmit-box-content-inner h3.pbmit-service-title').text();
		$(this).find('.pbmit-service-image-wrapper h3').text(f_letter.charAt(0));
	});	
}

function pbmit_iconbox_style16(){
	var pbmit1_var = $('.pbmit-ihbox-style-16');
	if (!pbmit1_var.length) {
		return;
	}
	pbmit1_var.each(function( index ) {
		var f_letter = $(this).find('.pbmit-element-title').text();
		$(this).find('.pbmit-ihbox-title-image .pbmit-element-title').text(f_letter.charAt(0));
	});	
}

function pbmit_horizontal_style() {
	var pbmit_var = $('.pbmit-element-portfolio-style-11');
	if (!pbmit_var.length) {
		return;
	}
	/*--------------------
	Vars
	--------------------*/ 
	const $menu = document.querySelector('.pbmit-element-portfolio-style-11 .pbmit-element-posts-wrapper')
	const $items = document.querySelectorAll('.pbmit-element-portfolio-style-11 .pbmit-portfolio-style-11')
	const $images = document.querySelectorAll('.pbmit-element-portfolio-style-11 .pbmit-image-wrapper')
	let menuWidth = $menu.clientWidth
	let itemWidth = $items[0].clientWidth
	let wrapWidth = $items.length * itemWidth

	let scrollSpeed = 0
	let oldScrollY = 0
	let scrollY = 0
	let y = 0


	/*--------------------
	Lerp
	--------------------*/
	const lerp = (v0, v1, t) => {
	return v0 * ( 1 - t ) + v1 * t
	}


	/*--------------------
	Dispose
	--------------------*/
	const dispose = (scroll) => {
	gsap.set($items, {
		x: (i) => {
		return i * itemWidth + scroll
		},
		modifiers: {
		x: (x, target) => {
			const s = gsap.utils.wrap(-itemWidth, wrapWidth - itemWidth, parseInt(x))
			return `${s}px`
		}
		}
	})
	} 
	dispose(0)


	/*--------------------
	Wheel
	--------------------*/
	const handleMouseWheel = (e) => {
	scrollY -= e.deltaY * 0.9
	}


	/*--------------------
	Touch
	--------------------*/
	let touchStart = 0
	let touchX = 0
	let isDragging = false
	const handleTouchStart = (e) => {
	touchStart = e.clientX || e.touches[0].clientX
	isDragging = true
	$menu.classList.add('is-dragging')
	}
	const handleTouchMove = (e) => {
	if (!isDragging) return
	touchX = e.clientX || e.touches[0].clientX
	scrollY += (touchX - touchStart) * 2.5
	touchStart = touchX
	}
	const handleTouchEnd = () => {
	isDragging = false
	$menu.classList.remove('is-dragging')
	}


	/*--------------------
	Listeners
	--------------------*/
	$menu.addEventListener('mousewheel', handleMouseWheel)

	$menu.addEventListener('touchstart', handleTouchStart)
	$menu.addEventListener('touchmove', handleTouchMove)
	$menu.addEventListener('touchend', handleTouchEnd)

	$menu.addEventListener('mousedown', handleTouchStart)
	$menu.addEventListener('mousemove', handleTouchMove)
	$menu.addEventListener('mouseleave', handleTouchEnd)
	$menu.addEventListener('mouseup', handleTouchEnd)

	$menu.addEventListener('selectstart', () => { return false })


	/*--------------------
	Resize
	--------------------*/
	window.addEventListener('resize', () => {
	menuWidth = $menu.clientWidth
	itemWidth = $items[0].clientWidth
	wrapWidth = $items.length * itemWidth
	})


	/*--------------------
	Render
	--------------------*/
	const render = () => {
	requestAnimationFrame(render)
	y = lerp(y, scrollY, .1)
	dispose(y)
	
	scrollSpeed = y - oldScrollY
	oldScrollY = y
	
	gsap.to($items, {
		skewX: -scrollSpeed * .1,
		rotate: scrollSpeed * .01,
		scale: 1 - Math.min(100, Math.abs(scrollSpeed)) * 0.002
	})
	}
	render()

}

function pbmit_mask_video() {

	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {

			gsap.set(".pbmit-mask-video-style-1 .pbmitmove-text1", { xPercent: 30 },".pbmit-mask-video-style-2 .pbmitmove-text1", { xPercent: 100 } )
			gsap.set(".pbmit-mask-video-style-1 .pbmitmove-text2", { xPercent: -170 },".pbmit-mask-video-style-2 .pbmitmove-text2", { xPercent: -50, yPercent: 10, })

			//Mask style1
			gsap.to(".pbmit-mask-video-style-1 .pbmitmove-text1", {
				xPercent: -450,
				scrollTrigger: {
					scrub: true,
					start: "top bottom",
					end: "bottom top",
				}
			});

			gsap.to(".pbmit-mask-video-style-1 .pbmitmove-text2", {
				xPercent: 70,
				yPercent: -20,
				scrollTrigger: {
					trigger: ".pbmit-mask-video-style-1 .pbmitmove-text1",
					scrub: true,
					start: "top bottom",
					end: "bottom top",
				}
			});

			//Mask style2

			gsap.to(".pbmit-mask-video-style-2 .pbmitmove-text1", {
				xPercent: -230,
				scrollTrigger: {
					scrub: true,
					start: "top bottom",
					end: "bottom top",
				}
			});	
			
			gsap.to(".pbmit-mask-video-style-2 .pbmitmove-text2", {
				xPercent: 50,
				yPercent: 20,
				scrollTrigger: {
					trigger: ".pbmit-mask-video-style-2 .pbmitmove-text1",
					scrub: true,
					start: "top bottom",
					end: "bottom top",
				}
			});
		},
		"(max-width:992px)": function() {
			ScrollTrigger.getAll().forEach(pin => pin.kill(true));
		}
	});
}

function pbmit_moving_marquee(){

	var pbmit_var = $('.pbmit-element-marquee-movetext-style-1');
	if (!pbmit_var.length) {
		return;
	}
	class pbmit_move_text {
			
		constructor () {
		const textPath = document.querySelector("#pbmit-text-move");
		const textPathLength = textPath.getComputedTextLength();
		const pathLength = document.querySelector('#pbmitpath').getTotalLength();

		// then I checked when to restart the movement to fake an infinite loop.
		const distanceReset = (textPathLength/4) * 100 / pathLength;
		
		this.offset = 0;
	
		let self = this,
			wrap = gsap.utils.wrap(-distanceReset, 0),
			proxy = {
				get offset() {
				return self.offset;
				},
				set offset(value) {
				self.offset = value;
				textPath.setAttribute("startOffset", wrap(value) + "%");
				}
			};
		
		this.offsetTo = gsap.quickTo(proxy, "offset", {duration: 0.9, ease: "power3"});
		
		// this way I'll be able to remove the event listener later
		this.wheel = this.updateSentencePos.bind(this);
		this.startWheel()
		}
	
		startWheel() {
		window.addEventListener('wheel', this.wheel);
		}
		updateSentencePos(e) {
		this.offsetTo(this.offset - e.deltaY/10);
		}
	}
	new pbmit_move_text()
}
 
function pbmit_portfolio_style13(){
	
	ScrollTrigger.matchMedia({
		"(min-width: 767px)": function() {
			if (typeof Swiper !== 'undefined') {
				var swiper = new Swiper('.pbmit-element-portfolio-style-13 .pbmit-element-posts-wrapper .portfolio-container', {
					effect: 'coverflow',
					grabCursor: true,
					centeredSlides: true,
					loop: true,
					speed:3000,
					spaceBetween:250,
					slidesPerView: 2, // or 'auto'
					coverflowEffect: {
						rotate: 50,
						stretch: 0,
						depth: 200,
						modifier: 1,
						slideShadows : true,
					},
					navigation: {
						nextEl: '.swiper-button-next',
						prevEl: '.swiper-button-prev',
					}
				});
			}
		},
		"(max-width:767px)": function() {
			ScrollTrigger.getAll().forEach(swiper => swiper.kill(true));
		}
	});
}

function pbmit_active_hover() {
    var pbmit_var = $('.pbmit-element-service-style-10,.pbmit-element-miconheading-style-17');
    if (!pbmit_var.length) {
        return;
    }
    pbmit_var.each(function() {
        var pbmit_Class = '.pbmit-hover-inner li,article.pbmit-miconheading-style-17';
        $(this)
            .find(pbmit_Class).first()
            .addClass('pbmit-active');
        $(this)
            .find(pbmit_Class)
            .on('mouseover', function() {
                $(this).addClass('pbmit-active').siblings().removeClass('pbmit-active');
            });
    });
}

function pbmit_verticel_layered_pinning() {
	var pbmit_var = $('.pbmit-element-portfolio-style-15');
    if (!pbmit_var.length) {
        return;
    }
	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {

			let pbmitpanels = gsap.utils.toArray(".pbmit-element-portfolio-style-15 .pbminfotech-box-content");
			const spacer = 0;
		
			let pbmitheight = pbmitpanels[0].offsetHeight;
			/*let tops = pbmitpanels.map(pbmitpanel => ScrollTrigger.create({trigger: pbmitpanel, start: "top top"}));
			console.log(pbmitheight);*/
			pbmitpanels.forEach((pbmitpanel, i) => {
			ScrollTrigger.create({
				trigger: pbmitpanel, 
				start: () => "top top", 
				//end: () => "+=" + pbmitheight,
				endTrigger: '.pbmit-element-portfolio-style-15', 
				end: `bottom top+=${pbmitheight + (pbmitpanels.length * spacer)}`,
				pin: true, 
				pinSpacing: false, 
			});
			/*ScrollTrigger.create({
				trigger: pbmitpanel,
				start: () => "top top",
				endTrigger: '.pbmit-element-portfolio-style-15',
				end: `bottom top+=${200 + (pbmitpanel.length)}`,
				pin: true,
				pinSpacing: false, 
				invalidateOnRefresh: true,
			});*/
			});
		},
		"(max-width:992px)": function() {
			ScrollTrigger.getAll().forEach(pbmitpanels => pbmitpanels.kill(true));
		}
	});
 }
 
 
 
function pbmit_multihbox_move() {

	const pbmit_elm = gsap.utils.toArray('.pbmit-miconheading-style-17:nth-child(even),.pbmit-miconheading-style-17:nth-child(odd)');
	if (pbmit_elm.length == 0) return
	
	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {
			

			gsap.set(".pbmit-miconheading-style-17:nth-child(even)", { yPercent: 100, })
			gsap.set(".pbmit-miconheading-style-17:nth-child(odd)", { yPercent: -100, })

			
			gsap.to(".pbmit-miconheading-style-17:nth-child(even)", {
				yPercent: -50,
				scrollTrigger: {
					scrub: true,
					start: () => "top top", 
					end:() =>  "bottom top",
					scrub:1
				}
			});
			gsap.to(".pbmit-miconheading-style-17:nth-child(odd)", {
				yPercent: 50,
				scrollTrigger: {
					scrub: true,
					start:() =>  "top top",
					end: () => "bottom top",
					scrub:1
				}
			});
		},
		"(max-width:992px)": function() {
			ScrollTrigger.getAll().forEach(pin => pin.kill(true));
		}
	});
}

function pbmit_squire_image() {
	const pbmit_elm = gsap.utils.toArray('.pbmit-textimonial-bg-move');
	if (pbmit_elm.length == 0) return
	ScrollTrigger.matchMedia({
		"(min-width: 992px)": function() {
			pbmit_elm.forEach((box, i) => {
				let tl = gsap.timeline({
					scrollTrigger: {
						trigger: box,
						start: "top 80%",
						end: "+=700px",
						scrub: 1
					},
					defaults: { ease: "none" }
				});
				tl.fromTo(box, { clipPath: 'inset(0% 7% 0% 7%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 3 }) 
			});
		}
	});
}
	
ScrollTrigger.addEventListener("refresh", pbmit_title_animation);

ScrollTrigger.matchMedia({
	"(max-width: 1200px)": function() {
		ScrollTrigger.getAll().forEach(t => t.kill());
	}
});

jQuery(window).resize(function() {
	pbmit_portfolio_style5();
});

// on ready
$(document).ready(function() {
	pbmit_staticbox_hover();
	pbmit_active_hover();
	pbmit_portfolio_style5();
	pbmit_portfolio_effect();
	pbmit_tween_effect();
});
// on load
$(window).on('load', function(){
	pbmit_dot_masking();
	pbmit_dot_masking2();
	pbmit_dot_masking2_add_class();
	pbmit_gallery();
	pbmit_portfolio_style2();
	pbmit_portfolio_style3();
	pbmit_portfolio_style5();
	pbmit_portfolio_style8();
	pbmit_portfolio_style13();
	pbmit_service_style4();
	pbmit_title_animation();
	pbmit_special_heading();
	pbmit_hover_img();
	pbmit_img_animation();
	pbmit_sticky();
	pbmit_action_box();
	pbmit_verticle_slide_image();
	pbmit_vertical_style();
	pbmit_horizontal_style();
	pbmit_set_tooltip();
	pbmit_portfolio_effect();
	pbmit_tween_effect();
	pbmit_team_mask_animation();
	pbmit_button_hover();
	pbmit_button_hover_move();
	pbmit_reel_video();
	pbmit_mask_video();
	pbmit_sticky_menu();
	pbmit_moving_marquee();
	pbmit_iconbox_style16();
	pbmit_multihbox_move();
	pbmit_squire_image();
	pbmit_verticel_layered_pinning();
	// Init cursor
	const cursor = new Cursor();
	$('[data-magnetic]').each(function() { new Magnetic(this); });
	gsap.delayedCall(1, () =>
		ScrollTrigger.getAll().forEach((t) => {
			t.refresh();
		})
	);	 
});