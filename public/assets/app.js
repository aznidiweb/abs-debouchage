(function(){
  var d=document, root=d.documentElement, w=window;
  root.classList.add("js");
  var reduce=w.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
  var header=d.querySelector(".header");
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
