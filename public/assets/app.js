(function(){
  var d=document, root=d.documentElement, w=window;
  root.classList.add("js");
  var reduce=w.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
  var header=d.querySelector(".navbar")||d.querySelector(".header");
  function headerBottom(){return Math.max(0,Math.round(header.getBoundingClientRect().bottom));}

  /* ---------- Menu mobile ---------- */
  var burger=d.querySelector(".burger"), nav=d.querySelector(".nav");
  function closeNav(){nav.classList.remove("open");d.body.style.overflow="";burger.setAttribute("aria-expanded","false");}
  if(burger&&nav){
    burger.addEventListener("click",function(){
      nav.style.setProperty("--nav-top",headerBottom()+"px");
      var o=nav.classList.toggle("open");
      burger.setAttribute("aria-expanded",o); d.body.style.overflow=o?"hidden":"";
    });
    nav.addEventListener("click",function(e){if(e.target.closest("a"))closeNav();});
  }
  d.querySelectorAll(".dd>button").forEach(function(b){
    b.addEventListener("click",function(){var o=b.parentNode.classList.toggle("open");b.setAttribute("aria-expanded",o);});
  });
  d.addEventListener("click",function(e){d.querySelectorAll(".dd.open").forEach(function(x){if(!x.contains(e.target)&&w.innerWidth>959)x.classList.remove("open");});});
  d.addEventListener("keydown",function(e){if(e.key==="Escape"){d.querySelectorAll(".dd.open").forEach(function(x){x.classList.remove("open");});if(nav&&nav.classList.contains("open"))closeNav();}});


  /* ---------- Barre de navigation flottante ---------- */
  var navWrap=d.querySelector(".nav-wrap");
  function onScroll(){ if(navWrap) navWrap.classList.toggle("scrolled", w.scrollY>40); }
  w.addEventListener("scroll",onScroll,{passive:true}); onScroll();

  /* ---------- Diaporama du héros ---------- */
  d.querySelectorAll("[data-slider]").forEach(function(h){
    var slides=h.querySelectorAll(".slide"), txt=h.querySelectorAll(".slide-txt>div"), btns=h.querySelectorAll(".prog button");
    if(slides.length<2) return;
    var i=0, timer=null, DUR=7000;
    function show(n){
      i=(n+slides.length)%slides.length;
      slides.forEach(function(s,k){s.classList.toggle("on",k===i);});
      txt.forEach(function(t,k){t.classList.toggle("on",k===i);t.setAttribute("aria-hidden",k!==i);});
      btns.forEach(function(b,k){b.classList.remove("on");b.classList.toggle("done",k<i);b.setAttribute("aria-current",k===i?"true":"false");void b.offsetWidth;if(k===i)b.classList.add("on");});
    }
    var pauseBtn=h.querySelector(".pause"), paused=reduce, hold=false;
    var L=d.documentElement.lang.indexOf("nl")===0;
    function stop(){clearInterval(timer);timer=null;h.classList.add("is-paused");}
    function play(){ clearInterval(timer); timer=null; if(paused||hold||d.hidden){h.classList.add("is-paused");return;} h.classList.remove("is-paused"); timer=setInterval(function(){show(i+1);},DUR); }
    function setPaused(v){paused=v; if(pauseBtn){pauseBtn.setAttribute("aria-pressed",v);pauseBtn.innerHTML=v?ICON_PLAY:ICON_PAUSE;pauseBtn.setAttribute("aria-label",v?(L?"Diavoorstelling afspelen":"Relancer le diaporama"):(L?"Diavoorstelling pauzeren":"Mettre le diaporama en pause"));} if(v)stop(); else {show(i);play();}}
    var ICON_PAUSE=pauseBtn?pauseBtn.innerHTML:"", ICON_PLAY='<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 4 13 8-13 8z"/></svg>';
    if(pauseBtn)pauseBtn.addEventListener("click",function(){setPaused(!paused);});
    btns.forEach(function(b,k){b.addEventListener("click",function(){show(k);play();});});
    /* arrêt au survol et quand le focus clavier est dans le héros */
    h.addEventListener("mouseenter",function(){hold=true;stop();}); h.addEventListener("mouseleave",function(){hold=false;play();});
    h.addEventListener("focusin",function(){hold=true;stop();}); h.addEventListener("focusout",function(e){if(!h.contains(e.relatedTarget)){hold=false;play();}});
    d.addEventListener("visibilitychange",function(){ if(d.hidden) stop(); else play(); });
    show(0); if(reduce)setPaused(true); else play();
  });

  /* ---------- Apparition discrète ---------- */
  var els=d.querySelectorAll(".reveal");
  if(!reduce&&"IntersectionObserver" in w){
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target);}});},{rootMargin:"0px 0px -6% 0px"});
    els.forEach(function(el){el.style.transitionDelay=(Number(el.getAttribute("data-d"))||0)*60+"ms";io.observe(el);});
  } else els.forEach(function(el){el.classList.add("in");});

  /* ---------- Diagnostic express ---------- */
  d.querySelectorAll("[data-diag]").forEach(function(box){
    var D=JSON.parse(box.getAttribute("data-diag")), U=D.ui;
    var panels=box.querySelectorAll(".diag-panel"), bars=box.querySelectorAll(".diag-bar i"), stepLbl=box.querySelector("[data-steplabel]");
    var sitList=box.querySelector("[data-sits]"), res=box.querySelector("[data-result]");
    var where=box.querySelector("[name=where]"), name=box.querySelector("[name=name]"), err=box.querySelector(".field .err"), sent=box.querySelector(".diag-sent");
    var state={svc:null,sit:null};

    function go(n,focus){
      panels.forEach(function(p){p.hidden=Number(p.getAttribute("data-p"))!==n;});
      bars.forEach(function(b,i){b.classList.toggle("on",i<n);});
      stepLbl.textContent=U.step.replace("{n}",n);
      if(focus){var h=panels[n-1].querySelector("[tabindex='-1']");if(h)h.focus({preventScroll:true});
        if(box.getBoundingClientRect().top<headerBottom())box.scrollIntoView({behavior:reduce?"auto":"smooth",block:"start"});}
    }
    function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];});}

    function pickSvc(id,focus){
      state.svc=id; state.sit=null;
      box.querySelectorAll("[data-svc]").forEach(function(b){b.setAttribute("aria-pressed",b.getAttribute("data-svc")===id);});
      sitList.innerHTML=D.svc[id].sits.map(function(s,i){return '<button type="button" class="d-opt" data-sit="'+i+'"><span>'+esc(s[1])+'</span>'+U.chev+'</button>';}).join("");
      go(2,focus);
    }
    function pickSit(i){
      state.sit=i;
      var S=D.svc[state.svc], sev=S.sits[i][0], V=U.sev[sev];
      res.innerHTML='<div class="verdict '+sev+'">'+U.icons[sev]+'<div><strong>'+esc(V[0])+'</strong><p>'+esc(V[1])+'</p></div></div>'+
        '<div class="res-grid"><div class="res-box"><small>'+esc(U.price)+'</small>'+(S.price?'<b>'+esc(U.from)+' '+S.price+' €</b>':'<p>'+esc(U.price_q)+'</p>')+'</div>'+
        '<div class="res-box"><small>'+esc(U.wait)+'</small><p>'+esc(S.tip||U.wait_generic)+'</p></div></div>';
      sent.classList.remove("show");
      go(3,true);
    }
    box.querySelectorAll("[data-svc]").forEach(function(b){b.addEventListener("click",function(){pickSvc(b.getAttribute("data-svc"),true);});});
    sitList.addEventListener("click",function(e){var b=e.target.closest("[data-sit]");if(b)pickSit(Number(b.getAttribute("data-sit")));});
    box.querySelectorAll("[data-back]").forEach(function(b){b.addEventListener("click",function(){go(Number(b.getAttribute("data-back")),true);});});
    where.addEventListener("input",function(){if(where.value.trim()){err.classList.remove("show");where.removeAttribute("aria-invalid");}});

    box.querySelector("[data-send]").addEventListener("click",function(){
      var c=where.value.trim();
      if(!c){err.classList.add("show");where.setAttribute("aria-invalid","true");where.focus();return;}
      var S=D.svc[state.svc], sit=S.sits[state.sit], W=U.wa;
      var lines=[W.hello,"","• "+W.prob+" : "+S.name,"• "+W.sit+" : "+sit[1],"• "+W.lvl+" : "+U.sev[sit[0]][0],"• "+W.where+" : "+c];
      if(name.value.trim())lines.push("• "+W.name+" : "+name.value.trim());
      w.open("https://wa.me/"+D.num+"?text="+encodeURIComponent(lines.join("\n")),"_blank","noopener");
      sent.classList.add("show");
    });

    if(D.pre&&D.svc[D.pre])pickSvc(D.pre,false); else go(1,false);
  });
})();
