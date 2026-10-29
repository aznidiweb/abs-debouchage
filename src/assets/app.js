(function(){
  var d=document, root=d.documentElement, w=window;
  root.classList.add("js");
  /* « Réduire les animations » (réglage Windows/Mac) : on coupe seulement les gros mouvements
     (effet de pages empilées, défilement doux) ; les petites animations restent pour tout le monde. */
  var reduceBig=w.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
  var reduce=false;
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

  /* ---------- Pages empilées : la section qui part recule sous la suivante ---------- */
  (function(){
    if(reduceBig) return;
    var secs=[].slice.call(d.querySelectorAll("main>section"));
    if(secs.length<2) return;
    var items=secs.slice(0,-1).map(function(s,i){
      var dim=d.createElement("div"); dim.className="stk-dim"; dim.setAttribute("aria-hidden","true"); s.appendChild(dim);
      return {s:s, next:secs[i+1], wrap:s.querySelector(":scope>.wrap")||s.firstElementChild, dim:dim, p:-1};
    });
    var ticking=false;
    function run(){
      ticking=false; var vh=w.innerHeight;
      items.forEach(function(it){
        var t=it.next.getBoundingClientRect().top;
        var p=Math.min(1,Math.max(0,(vh*.7-t)/(vh*.7)));          /* 0 = la suivante n'est pas là, 1 = elle couvre l'écran */
        if(Math.abs(p-it.p)<.004) return; it.p=p;
        if(p<=0){ if(it.wrap)it.wrap.style.transform=""; it.dim.style.opacity=0; return; }
        if(it.wrap) it.wrap.style.transform="translate3d(0,"+(p*-28).toFixed(1)+"px,0) scale("+(1-p*.05).toFixed(4)+")";
        it.dim.style.opacity=(p*.42).toFixed(3);
      });
    }
    function onS(){ if(!ticking){ticking=true;requestAnimationFrame(run);} }
    w.addEventListener("scroll",onS,{passive:true}); w.addEventListener("resize",onS); run();
  })();

  /* ---------- Apparition discrète ---------- */
  var els=d.querySelectorAll(".reveal");
  if(!reduce&&"IntersectionObserver" in w){
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target);}});},{rootMargin:"0px 0px -6% 0px"});
    els.forEach(function(el){el.style.transitionDelay=(Number(el.getAttribute("data-d"))||0)*60+"ms";io.observe(el);});
  } else els.forEach(function(el){el.classList.add("in");});

  /* ---------- Carte de la zone d'intervention ---------- */
  d.querySelectorAll("[data-zones]").forEach(function(box){
    var map=box.querySelector(".zmap"), pin=box.querySelector(".zm-pin"), lbl=box.querySelector(".zm-lbl"), drop=box.querySelector(".zm-drop");
    var pipe=box.querySelector(".zm-pipe"), pipeC=box.querySelector(".zm-pipe-c"), pipeW=box.querySelector(".zm-pipe-w"), last=null;
    var shapes=box.querySelectorAll(".zm-shapes [data-z]"), chips=box.querySelectorAll(".zc");
    var zName=box.querySelector("[data-zname]"), zCp=box.querySelector("[data-zcp]"), live=box.querySelector(".zm-name");
    var byZ={}; shapes.forEach(function(p){byZ[p.getAttribute("data-z")]=p;});
    var order=Array.prototype.map.call(chips,function(c){return c.getAttribute("data-z");});
    var cur=null, tour=null, k=0, user=false, visible=false;

    function select(z,fromUser){
      var p=byZ[z]; if(!p) return; cur=z;
      shapes.forEach(function(s){s.classList.toggle("on",s===p);});
      chips.forEach(function(c){c.setAttribute("aria-pressed",c.getAttribute("data-z")===z);});
      p.parentNode.appendChild(p);                                   /* contour sélectionné au premier plan */
      var x=+p.getAttribute("data-x"), y=+p.getAttribute("data-y");
      if(last){                                                       /* le tuyau amène l'eau de la commune précédente à la nouvelle */
        var dx=x-last[0], dy=y-last[1], mx=(x+last[0])/2-dy*.25, my=(y+last[1])/2+dx*.25;
        var dd="M"+last[0]+" "+last[1]+"Q"+mx.toFixed(1)+" "+my.toFixed(1)+" "+x+" "+y;
        pipeC.setAttribute("d",dd); pipeW.setAttribute("d",dd);
        pipe.classList.remove("go"); void pipe.getBoundingClientRect(); pipe.classList.add("go");
      }
      last=[x,y];
      drop.classList.remove("fall"); void drop.getBoundingClientRect(); drop.classList.add("fall");
      pin.style.transform="translate("+x+"px,"+y+"px)";
      lbl.textContent=p.getAttribute("data-n");
      lbl.setAttribute("text-anchor",x<110?"start":x>490?"end":"middle");
      lbl.setAttribute("x",x<110?-8:x>490?8:0);
      live.setAttribute("aria-live",fromUser?"polite":"off");
      zName.textContent=p.getAttribute("data-n"); zCp.textContent=p.getAttribute("data-cp");
    }
    function stopTour(){clearInterval(tour);tour=null;}
    function startTour(){
      if(reduce||user||tour||!visible||d.hidden) return;
      tour=setInterval(function(){k=(k+1)%order.length;select(order[k],false);},2300);
    }
    function takeOver(z){user=true;stopTour();select(z,true);}
    function hov(z,on){
      var p=byZ[z]; if(p)p.classList.toggle("hov",on);
      chips.forEach(function(c){if(c.getAttribute("data-z")===z)c.classList.toggle("hov",on);});
    }
    shapes.forEach(function(p){
      var z=p.getAttribute("data-z");
      p.addEventListener("click",function(){takeOver(z);});
      p.addEventListener("mouseenter",function(){hov(z,true);if(w.matchMedia("(hover:hover)").matches)takeOver(z);});
      p.addEventListener("mouseleave",function(){hov(z,false);});
    });
    chips.forEach(function(c){
      var z=c.getAttribute("data-z");
      c.addEventListener("click",function(){takeOver(z);});
      c.addEventListener("mouseenter",function(){hov(z,true);});
      c.addEventListener("mouseleave",function(){hov(z,false);});
      c.addEventListener("focus",function(){hov(z,true);});
      c.addEventListener("blur",function(){hov(z,false);});
    });
    /* recherche : commune ou code postal */
    var find=box.querySelector("[data-zfind]"), empty=box.querySelector("[data-zempty]");
    function norm(t){return String(t).toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9]+/g," ").trim();}
    if(find){
      chips.forEach(function(c){c._k=norm(c.getAttribute("data-k"));});
      find.addEventListener("input",function(){
        var q=norm(find.value), hits=[];
        chips.forEach(function(c){var ok=!q||c._k.indexOf(q)>-1||c._k.replace(/ /g,"").indexOf(q.replace(/ /g,""))>-1;c.parentNode.hidden=!ok;if(ok)hits.push(c);});
        box.querySelectorAll(".zgroup").forEach(function(g){g.hidden=!g.querySelector("li:not([hidden])");});
        empty.hidden=!(q&&!hits.length);
        if(q&&(hits.length===1||/^\d{4}$/.test(q)&&hits.length)) takeOver(hits[0].getAttribute("data-z"));
      });
      find.addEventListener("keydown",function(e){
        if(e.key==="Enter"){e.preventDefault();var h=box.querySelector(".zlist li:not([hidden]) .zc");if(h)takeOver(h.getAttribute("data-z"));}
      });
      find.addEventListener("focus",function(){user=true;stopTour();});
    }
    /* relief qui suit la souris (ordinateur) */
    var stage=box.querySelector(".zm-stage"), svgEl=box.querySelector(".zm-svg");
    if(stage&&svgEl&&w.matchMedia("(hover:hover)").matches&&!reduceBig){
      stage.addEventListener("mousemove",function(ev){var r=stage.getBoundingClientRect(),px=(ev.clientX-r.left)/r.width-.5,py=(ev.clientY-r.top)/r.height-.5;
        svgEl.style.setProperty("--ry",(px*10).toFixed(2)+"deg");svgEl.style.setProperty("--rx",(24+py*-10).toFixed(2)+"deg");});
      stage.addEventListener("mouseleave",function(){svgEl.style.removeProperty("--ry");svgEl.style.removeProperty("--rx");});
    }
    select(order[3]||order[0],false); k=Math.max(0,order.indexOf(cur));
    setTimeout(function(){map.classList.add("ready");},2600);
    if("IntersectionObserver" in w){
      new IntersectionObserver(function(en){visible=en[0].isIntersecting; if(visible)setTimeout(startTour,1600); else stopTour();},{threshold:.3}).observe(map);
    }
    d.addEventListener("visibilitychange",function(){if(d.hidden)stopTour();else startTour();});
  });

  /* ---------- Scènes animées des pages services ---------- */
  d.querySelectorAll("[data-scene]").forEach(function(box){
    var b=box.querySelector(".sc-pause"), icoPause=b?b.innerHTML:"";
    if(b) b.addEventListener("click",function(){
      var p=box.classList.toggle("paused");
      b.setAttribute("aria-pressed",p); b.innerHTML=p?b.getAttribute("data-ico-play"):icoPause;
      b.setAttribute("aria-label",box.getAttribute(p?"data-play":"data-pause"));
    });
    if("IntersectionObserver" in w) new IntersectionObserver(function(en){box.classList.toggle("off",!en[0].isIntersecting);},{threshold:.1}).observe(box);
    d.addEventListener("visibilitychange",function(){box.classList.toggle("off",d.hidden);});
  });

  /* ---------- Cartes services : une goutte tombe quand la carte apparaît (mobile) ---------- */
  if(!reduce&&"IntersectionObserver" in w&&!(w.matchMedia&&matchMedia("(hover:hover)").matches)){
    var dio=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add("drip");dio.unobserve(x.target);}});},{threshold:.6});
    d.querySelectorAll(".sv").forEach(function(c){dio.observe(c);});
  }

  /* ---------- Effets « eau » ---------- */
  /* onde au toucher sur les boutons */
  d.addEventListener("pointerdown",function(ev){
    var b=ev.target.closest&&ev.target.closest(".btn,.d-opt"); if(!b||reduce) return;
    var r=b.getBoundingClientRect();
    [0,1].forEach(function(k){var s=d.createElement("span");s.className="rip"+(k?" r2":"");s.setAttribute("aria-hidden","true");
      s.style.left=(ev.clientX-r.left)+"px";s.style.top=(ev.clientY-r.top)+"px";b.appendChild(s);setTimeout(function(){s.remove();},1000);});
  },{passive:true});

  /* étapes reliées par un tuyau + tuyau de lecture sur le côté */
  var stepsEls=[].slice.call(d.querySelectorAll(".steps"));
  var spipe=null;
  if(d.body.scrollHeight>w.innerHeight*2){
    spipe=d.createElement("div");spipe.className="spipe";spipe.setAttribute("aria-hidden","true");
    spipe.innerHTML='<svg class="spipe-fau" viewBox="0 0 34 34"><path d="M34 9H16a7 7 0 0 0-7 7v8" fill="none" stroke="#94a3b8" stroke-width="7" stroke-linecap="round"/><path d="M34 9H16a7 7 0 0 0-7 7v8" fill="none" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round"/><rect x="5" y="22" width="8" height="5" rx="1.5" fill="#64748b"/><rect x="20" y="1" width="4" height="7" fill="#64748b"/><rect x="14" y="0" width="16" height="4" rx="2" fill="#c2410c"/></svg>'+
      '<i class="spipe-drop"></i><i class="spipe-drop d2"></i><span class="spipe-tube"><i class="spipe-water"></i><i class="spipe-rip"></i></span>';
    d.body.appendChild(spipe);
  }
  var wTick=false;
  function water(){
    wTick=false; var vh=w.innerHeight;
    stepsEls.forEach(function(st){
      var r=st.getBoundingClientRect(), lis=st.children, n=lis.length, vert=w.innerWidth<=520;
      var p=vert?(vh*.72-r.top)/r.height:(vh*.82-r.top)/(vh*.42);
      p=Math.max(0,Math.min(1,p)); if(reduce) p=r.top<vh?1:0;
      st.style.setProperty("--f",p.toFixed(3));
      var pw=st.parentNode; if(pw.classList.contains("steps-wrap")){pw.style.setProperty("--f",p.toFixed(3));pw.classList.toggle("flow",p>=.985);}
      for(var i=0;i<n;i++) lis[i].classList.toggle("lit",p>=(n>1?i/(n-1):0)-.02&&p>0);
    });
    if(spipe){var m=d.documentElement.scrollHeight-vh, pp=m>0?Math.max(.03,Math.min(1,w.scrollY/m)):0;
      spipe.style.setProperty("--p",pp.toFixed(3));
      var th=spipe.querySelector(".spipe-tube").offsetHeight; spipe.style.setProperty("--fall",Math.round(th*(1-pp)+6)+"px");}
  }
  function onWater(){if(!wTick){wTick=true;requestAnimationFrame(water);}}
  w.addEventListener("scroll",onWater,{passive:true}); w.addEventListener("resize",onWater); water();

  /* chiffres qui défilent */
  if("IntersectionObserver" in w){
    var cio=new IntersectionObserver(function(en){en.forEach(function(x){
      if(!x.isIntersecting) return; cio.unobserve(x.target);
      var el=x.target, m=el.textContent.match(/^(\d+)(.*)$/); if(!m||reduce) return;
      var to=+m[1], rest=m[2], t0=null;
      function f(t){if(!t0)t0=t; var k=Math.min(1,(t-t0)/1200), v=Math.round(to*(1-Math.pow(1-k,3))); el.textContent=v+rest; if(k<1)requestAnimationFrame(f);}
      requestAnimationFrame(f);
    });},{threshold:.6});
    d.querySelectorAll(".stats b").forEach(function(b){cio.observe(b);});
  }

  /* ---------- Badge « Ouvert maintenant » (heure de Bruxelles) ---------- */
  d.querySelectorAll(".brand-sub[data-open]").forEach(function(el){
    var lang=d.documentElement.lang||"fr";
    function tick(){
      try{var t=new Intl.DateTimeFormat(lang,{hour:"2-digit",minute:"2-digit",timeZone:"Europe/Brussels"}).format(new Date());
        el.innerHTML=el.getAttribute("data-open")+" · <b>"+t+"</b>"; el.classList.add("live");}catch(e){}
    }
    tick(); setInterval(tick,20000);
  });

  /* ---------- « Ça déborde ? » ---------- */
  var urg=d.getElementById("urgence"), urgFrom=null;
  if(urg&&urg.showModal){
    d.addEventListener("click",function(e){
      var t=e.target.closest("[data-urg]"); if(t){urgFrom=t; urg.showModal(); return;}
      if(e.target.closest("[data-urg-close]")) {urg.close(); return;}
      if(e.target===urg){var r=urg.getBoundingClientRect(); if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom) urg.close();}
    });
    urg.addEventListener("close",function(){ if(urgFrom) urgFrom.focus(); });
  } else d.querySelectorAll("[data-urg]").forEach(function(b){b.hidden=true;});

  /* ---------- Animations des cartes services : en pause hors écran ---------- */
  if("IntersectionObserver" in w){
    var mio=new IntersectionObserver(function(en){en.forEach(function(x){x.target.classList.toggle("off",!x.isIntersecting);});},{rootMargin:"80px"});
    d.querySelectorAll("[data-mini]").forEach(function(m){m.classList.add("off");mio.observe(m);});
  }

  /* ---------- Diagnostic express ---------- */
  d.querySelectorAll("[data-diag]").forEach(function(box){
    var D=JSON.parse(box.getAttribute("data-diag")), U=D.ui;
    var panels=box.querySelectorAll(".diag-panel"), bars=box.querySelectorAll(".diag-bar i"), stepLbl=box.querySelector("[data-steplabel]");
    var sitList=box.querySelector("[data-sits]"), res=box.querySelector("[data-result]");
    var where=box.querySelector("[name=where]"), name=box.querySelector("[name=name]"), err=box.querySelector(".field .err"), sent=box.querySelector(".diag-sent");
    var state={svc:null,sit:null};

    function go(n,focus){
      panels.forEach(function(p){p.hidden=Number(p.getAttribute("data-p"))!==n;});
      box.setAttribute("data-step",n);
      bars.forEach(function(b,i){b.classList.toggle("on",i<n);});
      stepLbl.textContent=U.step.replace("{n}",n);
      if(focus){var h=panels[n-1].querySelector("[tabindex='-1']");if(h)h.focus({preventScroll:true});
        if(box.getBoundingClientRect().top<headerBottom())box.scrollIntoView({behavior:reduceBig?"auto":"smooth",block:"start"});}
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
