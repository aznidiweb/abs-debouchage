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
  /* barre transparente : on regarde la couleur du fond juste sous la barre pour choisir texte clair ou foncé */
  function bgLum(el){
    for(;el&&el!==d.documentElement;el=el.parentElement){
      var c=getComputedStyle(el).backgroundColor.match(/[\d.]+/g);
      if(c&&(c.length<4||+c[3]>.5)) return (0.299*c[0]+0.587*c[1]+0.114*c[2])/255;
    }
    return 1;
  }
  var navTick=false;
  function navTone(){
    navTick=false; if(!navWrap) return;
    var bar=navWrap.querySelector(".navbar"); if(!bar) return;
    var r=bar.getBoundingClientRect(), y=46;
    var br=bar.querySelector(".brand"), bx=br?br.getBoundingClientRect():r;
    /* lecture seule (aucun style modifié avant de mesurer) : pas de recalcul forcé de la mise en page */
    function pick(x){
      if(!d.elementsFromPoint) return null;
      var a=d.elementsFromPoint(x,Math.round(y));
      for(var i=0;i<a.length;i++){ if(!navWrap.contains(a[i])) return a[i]; }
      return null;
    }
    var under=pick(Math.round(Math.max(2,bx.left-6)))||pick(Math.round(w.innerWidth/2));
    if(under) navWrap.classList.toggle("on-light",bgLum(under)>.6);
  }
  var lastY=w.scrollY;
  function onScroll(){
    var y=w.scrollY;
    if(navWrap){
      navWrap.classList.toggle("scrolled", y>40);
      /* mobile : cachée quand on descend, revient dès qu'on remonte (la barre du bas garde le bouton Appeler) */
    }
    if(!navTick){navTick=true;requestAnimationFrame(navTone);}
  }
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
      lbl.textContent=(z==="bxl")?"":p.getAttribute("data-n");   /* Bruxelles-Capitale est déjà écrit sur la carte */
      lbl.setAttribute("text-anchor",x<110?"start":x>490?"end":"middle");
      lbl.setAttribute("x",x<110?-8:x>490?8:0);
      live.setAttribute("aria-live",fromUser?"polite":"off");
      zName.textContent=p.getAttribute("data-n"); zCp.textContent=p.getAttribute("data-cp");
      var zc=box.querySelector("[data-zcall]"); if(zc) zc.textContent=p.getAttribute("data-n");
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
    if(false){
      stage.addEventListener("mousemove",function(ev){var r=stage.getBoundingClientRect(),px=(ev.clientX-r.left)/r.width-.5,py=(ev.clientY-r.top)/r.height-.5;
        svgEl.style.setProperty("--ry",(px*10).toFixed(2)+"deg");svgEl.style.setProperty("--rx",(24+py*-10).toFixed(2)+"deg");});
      stage.addEventListener("mouseleave",function(){svgEl.style.removeProperty("--ry");svgEl.style.removeProperty("--rx");});
    }
    /* code postal belge → province */
    var cpIn=box.querySelector("[data-zcp-in]"), cpMsg=box.querySelector("[data-zcp-msg]"), cpMap={};
    try{cpMap=JSON.parse(box.getAttribute("data-cpmap")||"{}");}catch(e){}
    if(cpIn){
      cpIn.addEventListener("focus",function(){user=true;stopTour();});
      cpIn.addEventListener("input",function(){
        var v=cpIn.value.replace(/\D/g,"").slice(0,4); cpIn.value=v;
        if(v.length<4){cpMsg.hidden=true;return;}
        var n=+v, hit=null;
        Object.keys(cpMap).forEach(function(k){cpMap[k].forEach(function(r){if(n>=r[0]&&n<=r[1])hit=k;});});
        cpMsg.hidden=false;
        if(hit){takeOver(hit); cpMsg.className="zcp-msg ok"; cpMsg.textContent=cpIn.getAttribute("data-ok")+" ("+byZ[hit].getAttribute("data-n")+")";}
        else{cpMsg.className="zcp-msg bad"; cpMsg.textContent=cpIn.getAttribute("data-bad");}
      });
    }
    select(order[0],false); k=Math.max(0,order.indexOf(cur));
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

  /* ---------- Vidéo du héros : lecture en boucle ; sinon animation image (téléphones qui bloquent les vidéos) ---------- */
  d.querySelectorAll(".hp-video").forEach(function(v){
    var img=v.parentNode.querySelector(".hp-anim"), ok=false, swapped=false;
    v.muted=true; v.defaultMuted=true; v.loop=true; v.playsInline=true; v.setAttribute("muted",""); v.setAttribute("playsinline","");
    function swap(){ if(ok||swapped||!img) return; swapped=true; img.src=img.getAttribute("data-src"); img.hidden=false; v.style.visibility="hidden"; try{v.pause();}catch(e){} }
    function go(){ if(swapped) return; var p=v.play(); if(p&&p.then) p.then(function(){ok=true;}).catch(function(){ if(!ok) swap(); }); }
    v.addEventListener("playing",function(){ ok=true; v.classList.add("on"); });
    /* synchro : le bouchon saute vers 4 s dans la boucle -> petit éclat sur le bouton d'appel */
    var call=v.closest(".hero-video")&&v.closest(".hero-video").querySelector(".cta-row .btn-call"), lastT=0, BURST=4.0;
    if(call) v.addEventListener("timeupdate",function(){
      var t=v.currentTime;
      if(lastT<BURST&&t>=BURST&&t<BURST+.6){ call.classList.remove("burst"); void call.offsetWidth; call.classList.add("burst"); }
      lastT=t;
    });
    v.addEventListener("ended",function(){ v.currentTime=0; go(); });
    v.addEventListener("pause",function(){ if(!d.hidden&&!swapped) setTimeout(go,250); });
    d.addEventListener("visibilitychange",function(){ if(!d.hidden) go(); });
    go(); if(v.readyState<2) v.addEventListener("canplay",go,{once:true});
    setTimeout(function(){ if(!ok&&(v.paused||v.currentTime===0)) swap(); },1200);
  });

  /* ---------- Titres : s'écrivent lettre par lettre, chaque lettre se forme comme une goutte ---------- */
  function typeIt(t, delay, step){
    if(t.dataset.typed) return; t.dataset.typed="1";
    var original=t.innerHTML;
    if(!t.getAttribute("aria-label")) t.setAttribute("aria-label",t.textContent.replace(/\s+/g," ").trim());
    var n=0;
    function wrap(node,host){
      node.textContent.split(/(\s+)/).forEach(function(part){
        if(!part) return;
        if(/^\s+$/.test(part)){ host.appendChild(d.createTextNode(" ")); n++; return; }
        var wd=d.createElement("span"); wd.className="tw-w"; wd.setAttribute("aria-hidden","true");
        Array.prototype.forEach.call(part,function(ch){ var c=d.createElement("span"); c.className="tw-c"; c.textContent=ch; c.style.animationDelay=(delay+n*step)+"ms"; n++; wd.appendChild(c); });
        host.appendChild(wd);
      });
    }
    Array.prototype.slice.call(t.childNodes).forEach(function(node){
      if(node.nodeType===3){ var f=d.createDocumentFragment(); wrap(node,f); t.replaceChild(f,node); }
      else if(node.nodeType===1){ var txt=node.textContent; node.textContent=""; wrap({textContent:txt},node); }
    });
    t.classList.add("tw-on");
    /* une fois écrit, le titre redevient du texte normal (pas de scintillement sur iPhone) */
    setTimeout(function(){ t.innerHTML=original; t.classList.add("tw-done"); }, delay+n*step+900);
  }
  d.querySelectorAll(".hp-title").forEach(function(t){ typeIt(t,250,55); });
  /* ---------- Fluidité : toutes les animations d'une section s'arrêtent quand elle n'est pas à l'écran ---------- */
  if("IntersectionObserver" in w){
    var offIO=new IntersectionObserver(function(en){en.forEach(function(x){x.target.classList.toggle("is-off",!x.isIntersecting);});},{rootMargin:"150px 0px"});
    d.querySelectorAll("main>section,footer").forEach(function(sec){offIO.observe(sec);});
  }

  /* pied de page : sur mobile, la liste des services est repliée (les liens restent dans la page) */
  if(w.matchMedia("(max-width:760px)").matches) d.querySelectorAll(".fc-dt").forEach(function(x){x.open=false;});

  /* diagnostic : à l'arrivée sur la section, les choix s'allument une fois pour inviter à toucher */
  if("IntersectionObserver" in w) d.querySelectorAll("[data-diag]").forEach(function(box){
    var io2=new IntersectionObserver(function(en){ if(en[0].isIntersecting){ io2.disconnect(); setTimeout(function(){ box.classList.add("dg-hint"); setTimeout(function(){box.classList.remove("dg-hint");},2400); },500); } },{threshold:.55});
    io2.observe(box);
  });

  /* ---------- Google Ads : consentement + mesure des clics d'appel et WhatsApp ----------
     Rien n'est chargé chez Google tant que le visiteur n'a pas cliqué « Accepter ». */
  (function(){
    var cfg=w.ABS_ADS, bar=d.querySelector(".ck-bar"); if(!cfg||!cfg.id||!bar) return;
    var KEY="abs-consent", st=null; try{st=localStorage.getItem(KEY);}catch(e){}
    var loaded=false;
    function load(){
      if(loaded) return; loaded=true;
      w.dataLayer=w.dataLayer||[]; w.gtag=function(){w.dataLayer.push(arguments);};
      w.gtag("consent","default",{ad_storage:"granted",ad_user_data:"granted",ad_personalization:"denied",analytics_storage:"denied"});
      w.gtag("js",new Date()); w.gtag("config",cfg.id);
      var s=d.createElement("script"); s.async=true; s.src="https://www.googletagmanager.com/gtag/js?id="+encodeURIComponent(cfg.id); d.head.appendChild(s);
    }
    function conv(label){ if(loaded&&label&&w.gtag) w.gtag("event","conversion",{send_to:cfg.id+"/"+label}); }
    d.addEventListener("click",function(ev){
      var a=ev.target.closest&&ev.target.closest("a[href]"); if(!a) return;
      var h=a.getAttribute("href")||"";
      if(h.indexOf("tel:")===0) conv(cfg.call);
      else if(h.indexOf("wa.me/")>-1||h.indexOf("whatsapp")>-1) conv(cfg.wa);
    },true);
    function hide(){ bar.classList.remove("show"); setTimeout(function(){bar.hidden=true;},350); }
    if(st==="1"){ load(); return; }
    if(st==="0") return;
    /* le bandeau arrive après un petit défilement : il ne cache jamais le titre ni le bouton d'appel */
    var shown=false;
    function show(){ if(shown) return; shown=true; w.removeEventListener("scroll",onS); bar.hidden=false; requestAnimationFrame(function(){requestAnimationFrame(function(){bar.classList.add("show");});}); }
    function onS(){ if(w.scrollY>w.innerHeight*.6) show(); }
    w.addEventListener("scroll",onS,{passive:true}); setTimeout(show,6000);
    bar.querySelectorAll("[data-ck]").forEach(function(btn){ btn.addEventListener("click",function(){
      var v=btn.getAttribute("data-ck"); try{localStorage.setItem(KEY,v);}catch(e){}
      if(v==="1") load(); hide();
    }); });
  })();

  /* ---------- Fiche Google : la carte ne se charge que sur clic (aucun cookie Google avant) ---------- */
  d.querySelectorAll("[data-gmap]").forEach(function(box){
    var b=box.querySelector(".gm-load"); if(!b) return;
    b.addEventListener("click",function(){
      if(box.classList.contains("is-on")) return;
      var f=d.createElement("iframe"); f.src=box.getAttribute("data-gmap"); f.title=box.getAttribute("data-gtitle")||"Google Maps";
      f.loading="lazy"; f.referrerPolicy="no-referrer-when-downgrade"; f.setAttribute("allowfullscreen","");
      box.appendChild(f); box.classList.add("is-on");
    });
  });

  /* ---------- Mobile : listes repliables (services, communes) ---------- */
  function toggler(sel, cls){
    d.querySelectorAll(sel).forEach(function(b){
      var label=b.firstChild.textContent;
      b.addEventListener("click",function(){
        var host=b.parentNode, o=!host.classList.contains(cls);
        host.classList.toggle(cls,o); b.setAttribute("aria-expanded",o);
        b.firstChild.textContent=o?(d.documentElement.lang.indexOf("nl")===0?"Minder tonen":"Afficher moins"):label;
      });
    });
  }
  toggler("[data-svcmore]","svc-open");
  toggler("[data-zmore]","z-open");
  /* la recherche de commune ouvre la liste */
  d.querySelectorAll("[data-zfind]").forEach(function(f){ f.addEventListener("input",function(){ var h=f.closest(".zside"); if(h&&f.value.trim()) h.classList.add("z-open"); }); });

  /* ---------- Apparition des textes et des boutons ---------- */
  (function(){
    if(!("IntersectionObserver" in w)) return;
    var sel="main .sh p, main .sh .chip, main .cta-row, main .btn-lg:not(.cta-row .btn), main .zsearch, main .faq details, main .band p, .hp-lead, .hp-checks, .urg-btn, .hlabel";
    var els=[].slice.call(d.querySelectorAll(sel));
    els.forEach(function(el){ if(!el.closest(".tw-on")) el.classList.add("rise"); });
    var rio=new IntersectionObserver(function(en){en.forEach(function(x){ if(x.isIntersecting){ x.target.classList.add("risen"); rio.unobserve(x.target);} });},{rootMargin:"0px 0px -8% 0px"});
    els.forEach(function(el,i){ var sib=el.parentElement?[].indexOf.call(el.parentElement.children,el):0; el.style.setProperty("--rd",(Math.min(sib,6)*70)+"ms"); });
    /* héros : les éléments arrivent après le titre */
    d.querySelectorAll(".hero-video .hp-lead,.hero-video .cta-row,.hero-video .urg-btn,.hero-video .hp-checks").forEach(function(el,i){ el.style.setProperty("--rd",(250+i*110)+"ms"); });
    d.querySelectorAll(".hero-video .hlabel").forEach(function(el){ el.style.setProperty("--rd","100ms"); });
    /* on laisse le navigateur afficher l'état de départ avant de lancer les apparitions */
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ els.forEach(function(el){ rio.observe(el); }); }); });
  })();

  /* ---------- Zones : carte réelle + « Où êtes-vous ? » (commune ou code postal) ---------- */
  d.querySelectorAll("[data-zones2]").forEach(function(box){
    var Z={}; try{Z=JSON.parse(box.getAttribute("data-zd"));}catch(e){return;}
    var D=Z.prov||{};
    var pin=box.querySelector("[data-ompin]"), nm=box.querySelector("[data-zname]"), cp=box.querySelector("[data-zcp]");
    var form=box.querySelector("[data-zform]"), inp=box.querySelector("[data-zcp-in]"), msg=box.querySelector("[data-zcp-msg]");
    var done=box.querySelector("[data-zdone]"), btns=box.querySelectorAll("[data-zp]");
    function norm(s){return String(s).toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9]+/g," ").trim();}
    var N={}; Object.keys(Z.names||{}).forEach(function(k){N[norm(k)]=[Z.names[k],k];});
    function rng(r){return r.map(function(a){return a[0]+"–"+a[1];}).join(", ");}
    function mark(id){
      var p=D[id]; if(!p) return;
      pin.style.left=p.p[0]+"%"; pin.style.top=p.p[1]+"%"; box.classList.add("has-sel");
      btns.forEach(function(b){ var on=b.getAttribute("data-zp")===id; if(b.tagName==="BUTTON") b.setAttribute("aria-pressed",on); else b.classList.toggle("on",on); });
      var pl=box.querySelector("[data-ompl]"); if(pl) pl.textContent=p.n;
      pin.classList.toggle("lbl-below",p.p[1]<26); pin.classList.toggle("lbl-left",p.p[0]>80); pin.classList.toggle("lbl-right",p.p[0]<20);
      box.classList.remove("pin-drop"); void box.offsetWidth; box.classList.add("pin-drop");
    }
    function ok(id,label){
      mark(id); var p=D[id];
      nm.textContent=label||p.n; cp.textContent=(label&&label!==p.n)?"· "+p.n:"";
      msg.hidden=true; form.hidden=true; done.hidden=false; box.classList.add("is-done");
    }
    function find(v){
      var digits=v.replace(/\D/g,"");
      if(/^\d{4}$/.test(v.trim())||digits.length===4&&v.replace(/[\s\d]/g,"").length===0){
        var n=parseInt(digits,10);
        for(var id in D){ if(D[id].cp.some(function(r){return n>=r[0]&&n<=r[1];})) return [id,(Z.cps&&Z.cps[digits])?digits+" "+Z.cps[digits]:digits]; }
        return null;
      }
      var q=norm(v); if(q.length<2) return null;
      if(N[q]) return [N[q][0],N[q][1]];
      for(var k in N){ if(q.length>2&&k.indexOf(q)===0) return [N[k][0],N[k][1]]; }   /* début de nom : « ixel » -> Ixelles */
      return null;
    }
    function check(){
      var v=inp.value||""; if(!v.trim()){ inp.focus(); return; }
      var r=find(v);
      if(!r){ msg.textContent=inp.getAttribute("data-bad"); msg.hidden=false; return; }
      ok(r[0],r[1]);
    }
    form.addEventListener("submit",function(e){ e.preventDefault(); check(); inp.blur(); });
    inp.addEventListener("input",function(){ msg.hidden=true; if(N[norm(inp.value)]) check(); });
    btns.forEach(function(b){ b.addEventListener("click",function(){ ok(b.getAttribute("data-zp")); }); });
    box.querySelector("[data-zchg]").addEventListener("click",function(){ done.hidden=true; form.hidden=false; box.classList.remove("is-done"); inp.value=""; inp.focus(); });
  });

  /* ---------- FAQ : sur ordinateur, la réponse s'affiche à droite ---------- */
  d.querySelectorAll("[data-fq]").forEach(function(fq){
    var items=[].slice.call(fq.querySelectorAll(".fq-i")), panel=fq.querySelector(".fq-panel"), mq=w.matchMedia("(min-width:960px)");
    if(!items.length||!panel) return;
    var all=fq.querySelector("[data-fqall]");
    if(all){ var more=all.firstChild.textContent, less=(d.documentElement.lang.indexOf("nl")===0?"Minder tonen":"Voir moins");
      all.setAttribute("aria-expanded","false");
      all.addEventListener("click",function(){
        var o=!fq.classList.contains("fq-open"); fq.classList.toggle("fq-open",o); all.setAttribute("aria-expanded",o);
        all.firstChild.textContent=o?less:more;
        if(!o){ items.forEach(function(x,i){ if(i>3) x.open=false; }); var r=fq.getBoundingClientRect(); if(r.top<0) fq.scrollIntoView({block:"start"}); }
      }); }
    function show(it){
      items.forEach(function(x){ x.classList.toggle("is-on",x===it); });
      var q=it.querySelector(".fq-q").textContent, a=it.querySelector(".fq-a").innerHTML, g=it.getAttribute("data-g");
      panel.innerHTML='<div class="fq-in">'+(g?'<span class="fq-tag">'+g.replace(/</g,"&lt;")+'</span>':'')+'<h3>'+q.replace(/</g,"&lt;")+'</h3>'+a+'</div>';
    }
    function mode(){
      var split=mq.matches; fq.classList.toggle("is-split",split); panel.hidden=!split;
      if(split){ items.forEach(function(x){x.open=false;}); show(fq.querySelector(".fq-i.is-on")||items[0]); }
    }
    items.forEach(function(it){
      it.querySelector("summary").addEventListener("click",function(e){ if(mq.matches){ e.preventDefault(); show(it); } });
    });
    if(mq.addEventListener) mq.addEventListener("change",mode); else if(mq.addListener) mq.addListener(mode);
    mode();
  });

  /* ---------- Demande d'intervention (6 étapes) ----------
     Envoi direct vers /api/demande quand le serveur est configuré ; sinon la demande part par WhatsApp,
     déjà rédigée. Jamais de faux « envoyé » : le message de réussite n'apparaît que sur réponse positive du serveur. */
  d.querySelectorAll("[data-req]").forEach(function(box){
    var D=JSON.parse(box.getAttribute("data-req")), U=D.ui, T=U.steps.length, E=U.err;
    var form=box.querySelector("[data-form]"), panels={}, cur=1, dir=1, editing=false, ready=false, sending=false;
    box.querySelectorAll(".rq-p").forEach(function(p){ panels[p.getAttribute("data-p")]=p; });
    var bars=box.querySelectorAll(".rq-prog i"), lbl=box.querySelector("[data-steplabel]"), lname=box.querySelector("[data-stepname]");
    var KEY="abs-demande-"+D.lang, photos=[], MAXP=4, MAXIN=20*1024*1024;
    var f=function(n){ return form.querySelector("[name='"+n+"']"); };
    var probs={}; D.probs.forEach(function(p){ probs[p.id]=p; });
    var st={problem:null,sit:null,urgency:null,desc:"",cp:"",city:"",addr:"",name:"",tel:"",mail:"",consent:false,step:1};

    function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];});}
    function save(){ try{ sessionStorage.setItem(KEY,JSON.stringify(st)); }catch(e){} }
    function load(){ try{ var s=JSON.parse(sessionStorage.getItem(KEY)||"null"); if(s&&typeof s==="object") for(var k in st) if(k in s) st[k]=s[k]; }catch(e){} }
    function clear(){ try{ sessionStorage.removeItem(KEY); }catch(e){} }

    /* ---- validation ---- */
    var cpOk=function(v){ return /^[1-9][0-9]{3}$/.test(v); };
    function telNorm(v){ return String(v||"").replace(/[\s.\-\/()]/g,""); }
    var telOk=function(v){ var t=telNorm(v); return /^(\+|00)[1-9][0-9]{7,14}$/.test(t)||/^0[1-9][0-9]{7,8}$/.test(t); };
    var mailOk=function(v){ return !v||/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v); };
    function region(cp){ var n=parseInt(cp,10); if(!n) return "";
      if(n>=1000&&n<=1299) return "bxl"; if((n>=1300&&n<=1499)||(n>=4000&&n<=7999)) return "wal"; return "vl"; }
    function setErr(name,msg){
      var p=form.querySelector("[data-err='"+name+"']"), i=f(name);
      if(p){ p.textContent=msg||""; p.classList.toggle("show",!!msg); }
      if(i&&i.type!=="radio"){ if(msg) i.setAttribute("aria-invalid","true"); else i.removeAttribute("aria-invalid"); }
      return !msg;
    }
    var checks={
      1:function(){ return setErr("problem",st.problem?"":E.prob); },
      2:function(){ return setErr("urgency",st.urgency?"":E.urg); },
      3:function(){ var a=setErr("cp",cpOk(st.cp)?"":E.cp), b=setErr("city",st.city.trim().length>=2?"":E.city); return a&&b; },
      4:function(){ return true; },
      5:function(){ var a=setErr("name",st.name.trim().length>=2?"":E.name), b=setErr("tel",telOk(st.tel)?"":E.tel), c=setErr("mail",mailOk(st.mail.trim())?"":E.mail), k=setErr("consent",st.consent?"":E.consent); return a&&b&&c&&k; }
    };
    function firstInvalid(n){ var x=panels[n].querySelector("[aria-invalid=true]")||panels[n].querySelector(".rq-err.show"); if(!x) return;
      var t=x.matches("input,textarea")?x:(panels[n].querySelector("input:not([type=hidden])")); if(t) t.focus(); }

    /* ---- navigation ---- */
    function go(n,focus){
      var key=String(n), prev=panels[String(cur)];
      dir=(typeof n==="number"&&typeof cur==="number"&&n<cur)?-1:1;
      for(var k in panels) panels[k].hidden=(k!==key);
      var p=panels[key]; p.classList.remove("rq-in","rq-in-b"); void p.offsetWidth; if(!reduceBig) p.classList.add(dir>0?"rq-in":"rq-in-b");
      cur=n; box.setAttribute("data-step",key);
      var num=typeof n==="number"?n:T;
      bars.forEach(function(b,i){ b.classList.toggle("on",i<num); b.classList.toggle("now",i===num-1); });
      if(typeof n==="number"){ lbl.textContent=U.step.replace("{n}",n).replace("{t}",T); lname.textContent=U.steps[n-1]; }
      box.querySelectorAll("[data-nextlbl]").forEach(function(s){ s.textContent=editing?U.back_recap:U.next; });
      if(n===6) recap();
      if(focus){ var h=p.querySelector(".rq-q"); if(h) h.focus({preventScroll:true});
        if(box.getBoundingClientRect().top<headerBottom()) box.scrollIntoView({behavior:reduceBig?"auto":"smooth",block:"start"}); }
      if(typeof n==="number"){ st.step=n; save(); }
    }
    function next(){ if(!checks[cur]()){ firstInvalid(cur); return; } if(editing&&cur<6){ editing=false; go(6,true); return; } go(cur+1,true); }
    box.querySelectorAll("[data-next]").forEach(function(b){ b.addEventListener("click",next); });
    box.querySelectorAll("[data-back]").forEach(function(b){ b.addEventListener("click",function(){ if(editing){ editing=false; } go(Math.max(1,cur-1),true); }); });
    form.addEventListener("keydown",function(ev){ if(ev.key==="Enter"&&ev.target.matches("input:not([type=checkbox]):not([type=radio]):not([type=file])")){ ev.preventDefault(); if(cur<6) next(); } });

    /* ---- étape 1 : problème ---- */
    function pickProblem(id,advance){
      st.problem=id; setErr("problem","");
      var r=form.querySelector("input[name=problem][value='"+id+"']"); if(r) r.checked=true;
      var P=probs[id], box2=form.querySelector("[data-sitsbox]"), wrap=form.querySelector("[data-sits]");
      if(st.sit!=null&&(!P.sits[st.sit])) st.sit=null;
      wrap.innerHTML=P.sits.map(function(s,i){ return '<button type="button" class="rq-chip" data-sit="'+i+'" aria-pressed="'+(st.sit===i)+'">'+esc(s[1])+'</button>'; }).join("");
      box2.hidden=!P.sits.length;
      form.querySelector("[data-tip]").textContent=P.tip||U.wait_generic;
      save(); if(advance) setTimeout(function(){ go(2,true); },reduceBig?0:220);
    }
    form.querySelectorAll("input[name=problem]").forEach(function(r){
      r.addEventListener("change",function(){ pickProblem(r.value,false); });
      r.closest("label").addEventListener("click",function(ev){ if(ev.detail>0) setTimeout(function(){ if(r.checked) go(2,true); },reduceBig?0:220); });
    });

    /* ---- étape 2 : urgence ---- */
    var SEV={urgent:"urgent",today:"urgent",plan:"soon"};
    function setUrg(v){ st.urgency=v; var r=form.querySelector("input[name=urgency][value='"+v+"']"); if(r) r.checked=true; setErr("urgency","");
      form.querySelector("[data-urgbox]").hidden=(v!=="urgent"); save(); }
    form.querySelector("[data-sits]").addEventListener("click",function(ev){
      var b=ev.target.closest("[data-sit]"); if(!b) return; var i=Number(b.getAttribute("data-sit"));
      st.sit=(st.sit===i)?null:i;
      form.querySelectorAll("[data-sit]").forEach(function(x){ x.setAttribute("aria-pressed",Number(x.getAttribute("data-sit"))===st.sit); });
      if(st.sit!=null) setUrg(SEV[probs[st.problem].sits[st.sit][0]]||"soon"); save();
    });
    form.querySelectorAll("input[name=urgency]").forEach(function(r){ r.addEventListener("change",function(){ setUrg(r.value); }); });

    /* ---- champs texte : sauvegarde + validation instantanée après la première erreur ---- */
    ["desc","cp","city","addr","name","tel","mail"].forEach(function(n){
      var i=f(n); if(!i) return;
      i.addEventListener("input",function(){
        st[n]=i.value;
        if(n==="cp"){ i.value=i.value.replace(/\D/g,"").slice(0,4); st.cp=i.value;
          var c=D.cp[st.cp], city=f("city"); if(c&&(!city.value.trim()||city.getAttribute("data-auto")==="1")){ city.value=c; st.city=c; city.setAttribute("data-auto","1"); setErr("city",""); } }
        if(n==="city") i.removeAttribute("data-auto");
        if(i.getAttribute("aria-invalid")==="true"){ var stp=n==="cp"||n==="city"?3:5; checks[stp](); }
        save();
      });
      i.addEventListener("blur",function(){
        if(!i.value) return;
        if(n==="cp") setErr("cp",cpOk(i.value)?"":E.cp);
        if(n==="tel") setErr("tel",telOk(i.value)?"":E.tel);
        if(n==="mail") setErr("mail",mailOk(i.value.trim())?"":E.mail);
      });
    });
    f("consent").addEventListener("change",function(){ st.consent=f("consent").checked; if(st.consent) setErr("consent",""); save(); });

    /* ---- étape 4 : photos (compressées dans le navigateur) ---- */
    var file=form.querySelector("[data-file]"), thumbs=form.querySelector("[data-thumbs]"), addLbl=form.querySelector("[data-addlbl]"), addCnt=form.querySelector("[data-addcount]"), addBtn=form.querySelector("[data-addbtn]");
    function compress(fl){
      return new Promise(function(res,rej){
        var u=URL.createObjectURL(fl), im=new Image();
        im.onload=function(){
          var M=1600, w0=im.naturalWidth, h0=im.naturalHeight, k=Math.min(1,M/Math.max(w0,h0)), cw=Math.round(w0*k), ch=Math.round(h0*k);
          var c=d.createElement("canvas"); c.width=cw; c.height=ch; var x=c.getContext("2d"); x.fillStyle="#fff"; x.fillRect(0,0,cw,ch); x.drawImage(im,0,0,cw,ch);
          URL.revokeObjectURL(u);
          (function enc(q){ c.toBlob(function(b){ if(!b) return rej(); if(b.size>1800000&&q>0.5) return enc(q-0.12); res(b); },"image/jpeg",q); })(0.8);
        };
        im.onerror=function(){ URL.revokeObjectURL(u); rej(); };
        im.src=u;
      });
    }
    function drawThumbs(){
      thumbs.innerHTML=photos.map(function(p,i){ return '<li><img src="'+p.url+'" alt="'+esc(U.photo_n.replace("{n}",i+1))+'"><button type="button" class="rq-rm" data-rm="'+i+'" aria-label="'+esc(U.rm+" "+(i+1))+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></li>'; }).join("");
      addCnt.textContent=photos.length+" / "+MAXP; addBtn.hidden=photos.length>=MAXP;
    }
    file.addEventListener("change",function(){
      var list=[].slice.call(file.files||[]); file.value=""; setErr("photos","");
      var room=MAXP-photos.length, msgs=[];
      if(list.length>room){ msgs.push(E.photo_max); list=list.slice(0,room); }
      var jobs=list.map(function(fl){
        if(!/^image\//.test(fl.type)&&!/\.(heic|heif)$/i.test(fl.name)){ msgs.push(E.photo_type); return Promise.resolve(); }
        if(fl.size>MAXIN){ msgs.push(E.photo_big); return Promise.resolve(); }
        return compress(fl).then(function(b){ if(photos.length<MAXP) photos.push({blob:b,url:URL.createObjectURL(b)}); },function(){ msgs.push(E.photo_read); });
      });
      addBtn.classList.add("busy");
      Promise.all(jobs).then(function(){ addBtn.classList.remove("busy"); drawThumbs(); if(msgs.length) setErr("photos",msgs.filter(function(m,i,a){return a.indexOf(m)===i;}).join(" ")); });
    });
    thumbs.addEventListener("click",function(ev){ var b=ev.target.closest("[data-rm]"); if(!b) return; var i=Number(b.getAttribute("data-rm"));
      URL.revokeObjectURL(photos[i].url); photos.splice(i,1); drawThumbs(); setErr("photos","");
      var nb=thumbs.querySelector("[data-rm]"); (nb||file).focus(); });

    /* ---- étape 6 : récapitulatif ---- */
    function urgLabel(){ return st.urgency?U.urg[st.urgency][0]:""; }
    function locLine(){ var r=region(st.cp); return [st.addr.trim(),(st.cp+" "+st.city.trim()).trim()].filter(Boolean).join(", ")+(r?" ("+U.region[r]+")":""); }
    function recap(){
      var P=probs[st.problem]||{label:""}, sit=(st.sit!=null&&P.sits&&P.sits[st.sit])?P.sits[st.sit][1]:"";
      var rows=[[1,U.r_prob,esc(P.label)+(sit?'<small>'+esc(sit)+'</small>':"")],[2,U.r_urg,esc(urgLabel())],[2,U.r_desc,st.desc.trim()?esc(st.desc.trim()):'<em>'+esc(U.nodesc)+'</em>'],
        [3,U.r_loc,esc(locLine())],[4,U.r_photos,photos.length?'<span class="rq-mini">'+photos.map(function(p){return '<img src="'+p.url+'" alt="">';}).join("")+'</span>':'<em>'+esc(U.none)+'</em>'],
        [5,U.r_contact,esc(st.name.trim())+'<small>'+esc(st.tel.trim())+(st.mail.trim()?" · "+esc(st.mail.trim()):"")+'</small>']];
      form.querySelector("[data-recap]").innerHTML=rows.map(function(r){ return '<div class="rq-ri"><div><span class="rq-rk">'+esc(r[1])+'</span><span class="rq-rv">'+r[2]+'</span></div><button type="button" class="rq-edit" data-edit="'+r[0]+'">'+esc(U.edit)+'</button></div>'; }).join("");
      box.querySelector("[data-sendlbl]").textContent=ready?U.send:U.send_wa;
      box.querySelector("[data-submit]").classList.toggle("btn-wa",!ready);
      box.querySelector("[data-wanote]").hidden=ready;
    }
    form.querySelector("[data-recap]").addEventListener("click",function(ev){ var b=ev.target.closest("[data-edit]"); if(!b) return; editing=true; go(Number(b.getAttribute("data-edit")),true); });

    /* ---- envoi ---- */
    function waText(){
      var W=U.wa, P=probs[st.problem], sit=(st.sit!=null&&P.sits[st.sit])?" ("+P.sits[st.sit][1]+")":"";
      var L=[W.hello,"","• "+W.prob+" : "+P.label+sit,"• "+W.urg+" : "+urgLabel(),"• "+W.where+" : "+locLine()];
      if(st.desc.trim()) L.push("• "+W.desc+" : "+st.desc.trim());
      L.push("• "+W.name+" : "+st.name.trim(),"• "+W.tel+" : "+st.tel.trim()); if(st.mail.trim()) L.push("• "+W.mail+" : "+st.mail.trim());
      if(photos.length) L.push("",W.photos);
      return L.join("\n");
    }
    function openWa(){ var A=w.ABS_ADS; if(A&&A.id&&A.wa&&w.gtag) w.gtag("event","conversion",{send_to:A.id+"/"+A.wa}); w.open("https://wa.me/"+D.num+"?text="+encodeURIComponent(waText()),"_blank","noopener"); }
    function allValid(){ for(var n=1;n<=5;n++) if(!checks[n]()){ editing=false; go(n,true); firstInvalid(n); return false; } return true; }
    function fmtDate(iso){ try{ return new Date(iso).toLocaleString(D.lang==="nl"?"nl-BE":"fr-BE",{dateStyle:"long",timeStyle:"short",timeZone:"Europe/Brussels"}); }catch(e){ return iso; } }
    function done(res){
      box.querySelector("[data-okp]").textContent=U.ok_p.replace("{tel}",st.tel.trim());
      box.querySelector("[data-okid]").textContent=res.id; box.querySelector("[data-okat]").textContent=fmtDate(res.receivedAt);
      box.querySelector("[data-okurg]").hidden=st.urgency!=="urgent";
      var P=probs[st.problem]; box.querySelector("[data-oktip]").textContent=(P&&P.tip)||U.wait_generic;
      try{ w.dispatchEvent(new CustomEvent("abs:lead",{detail:{id:res.id,urgency:st.urgency,problem:st.problem}})); }catch(e){}
      clear(); go("ok",true); box.querySelector(".rq-steplbl").hidden=true;
    }
    function fail(){ go("ko",true); }
    form.addEventListener("submit",function(ev){
      ev.preventDefault(); if(sending) return;
      if(!allValid()) return;
      if(!ready){ openWa(); var s=box.querySelector("[data-wasent]"); s.textContent=U.sent; s.hidden=false; return; }
      var fd=new FormData();
      ["problem","urgency","desc","cp","city","addr","name","tel","mail"].forEach(function(k){ fd.append(k,(st[k]||"").toString().trim()); });
      if(st.sit!=null&&probs[st.problem].sits[st.sit]) fd.append("situation",probs[st.problem].sits[st.sit][1]);
      fd.append("consent",st.consent?"1":"0"); fd.append("lang",D.lang); fd.append("page",location.pathname);
      fd.append("website",f("website").value||"");
      photos.forEach(function(p,i){ fd.append("photos",p.blob,"photo-"+(i+1)+".jpg"); });
      sending=true; var btn=box.querySelector("[data-submit]"), sl=box.querySelector("[data-sendlbl]"); btn.disabled=true; btn.classList.add("busy"); sl.textContent=U.sending;
      var ctrl=("AbortController" in w)?new AbortController():null, to=setTimeout(function(){ if(ctrl) ctrl.abort(); },45000);
      fetch(D.api,{method:"POST",body:fd,signal:ctrl?ctrl.signal:undefined,headers:{"Accept":"application/json"}})
        .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){ return {ok:r.ok,j:j}; }); })
        .then(function(x){ if(x.ok&&x.j&&x.j.ok&&x.j.id) done(x.j); else fail(); },fail)
        .then(function(){ clearTimeout(to); sending=false; btn.disabled=false; btn.classList.remove("busy"); sl.textContent=ready?U.send:U.send_wa; });
    });
    box.querySelector("[data-kowa]").addEventListener("click",openWa);
    box.querySelector("[data-retry]").addEventListener("click",function(){ go(6,true); });
    box.querySelector("[data-new]").addEventListener("click",function(){
      for(var k in st) st[k]=(k==="consent")?false:(k==="step")?1:(k==="problem"||k==="sit"||k==="urgency")?null:"";
      photos.forEach(function(p){ URL.revokeObjectURL(p.url); }); photos=[]; drawThumbs(); form.reset(); clear();
      box.querySelector(".rq-steplbl").hidden=false; form.querySelector("[data-urgbox]").hidden=true; form.querySelector("[data-sitsbox]").hidden=true; go(1,true);
    });

    /* ---- le serveur sait-il recevoir les demandes ? (sinon : WhatsApp, comme avant) ---- */
    try{ fetch(D.api,{headers:{"Accept":"application/json"},cache:"no-store"}).then(function(r){ return r.ok?r.json():null; }).then(function(j){ ready=!!(j&&j.ready); if(cur===6) recap(); },function(){}); }catch(e){}

    /* ---- reprise d'une demande en cours (même onglet) ---- */
    load();
    ["desc","cp","city","addr","name","tel","mail"].forEach(function(n){ if(f(n)) f(n).value=st[n]||""; });
    f("consent").checked=!!st.consent;
    var startPre=!st.problem&&D.pre&&probs[D.pre];
    if(st.problem&&probs[st.problem]) pickProblem(st.problem,false); else if(startPre) pickProblem(D.pre,false);
    if(st.urgency) setUrg(st.urgency);
    drawThumbs();
    var s0=Number(st.step)||1; if(s0===4||s0>5) s0=5; /* les photos ne sont pas gardées : on reprend avant le récapitulatif */
    var okTo=1; for(var n=1;n<s0;n++){ if(!checks[n]()) break; okTo=n+1; }
    ["problem","urgency","cp","city","name","tel","mail","consent"].forEach(function(n){ setErr(n,""); });
    go(st.problem?Math.min(okTo,s0):1,false);
  });
})();

/* ==========================================================================
   Immersion au défilement : les éléments bougent AVEC le doigt (et non une
   seule fois). Uniquement transform/opacity, une lecture puis une écriture
   par image, rien si l'utilisateur a demandé moins d'animations.
   ========================================================================== */
(function(){
  var w=window, d=document;
  if(!("IntersectionObserver" in w)||!w.requestAnimationFrame) return;
  if(w.matchMedia&&w.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var root=d.documentElement; root.classList.add("fx");
  var bar=d.createElement("div"); bar.className="sp"; bar.setAttribute("aria-hidden","true"); d.body.appendChild(bar);
  var hero=d.querySelector(".hero-video");
  var ent=[].slice.call(d.querySelectorAll(".svc-grid>li:not(.reveal),.pt-grid>*:not(.reveal),.pa-grid>.pa-i,.om,.dg-get>li,.b5-pipe"));
  var par=[].slice.call(d.querySelectorAll(".diag-sec,.band5"));
  var vh=w.innerHeight, heroH=hero?hero.offsetHeight:0, docH=root.scrollHeight, tick=false;
  function cl(x){return x<0?0:x>1?1:x;}
  var io=new IntersectionObserver(function(en){en.forEach(function(x){x.target._fx=x.isIntersecting;});ask();},{rootMargin:"25% 0px 25% 0px"});
  ent.forEach(function(el){el.classList.add("fxe");io.observe(el);});
  par.forEach(function(el){io.observe(el);});
  function frame(){
    tick=false;
    var y=w.scrollY||w.pageYOffset||0, i, el, r=[], q=[];
    /* lectures */
    for(i=0;i<ent.length;i++){el=ent[i]; if(el&&el._fx) r.push([i,el.getBoundingClientRect().top]);}
    for(i=0;i<par.length;i++){el=par[i]; if(el._fx){var b=el.getBoundingClientRect(); q.push([el,b.top,b.height]);}}
    docH=root.scrollHeight;   /* la page s'allonge quand les sections lointaines s'affichent */
    /* écritures */
    var max=docH-vh; bar.style.transform="scaleX("+(max>0?cl(y/max):0).toFixed(4)+")";
    if(hero&&heroH&&y<heroH*1.15) hero.style.setProperty("--hp",cl(y/heroH).toFixed(3));
    for(i=0;i<r.length;i++){
      el=ent[r[i][0]]; var e=cl((vh*.97-r[i][1])/(vh*.3));
      if(e>=1){el.classList.remove("fxe");el.style.removeProperty("--e");io.unobserve(el);ent[r[i][0]]=null;}   /* arrivé : on rend l'élément à ses styles normaux */
      else el.style.setProperty("--e",e.toFixed(3));
    }
    for(i=0;i<q.length;i++) q[i][0].style.setProperty("--p",cl((vh-q[i][1])/(vh+q[i][2])).toFixed(3));
  }
  function ask(){ if(!tick){tick=true;w.requestAnimationFrame(frame);} }
  w.addEventListener("scroll",ask,{passive:true});
  w.addEventListener("resize",function(){vh=w.innerHeight;heroH=hero?hero.offsetHeight:0;docH=root.scrollHeight;ask();});
  w.addEventListener("load",function(){docH=root.scrollHeight;ask();});
  ask();
})();
