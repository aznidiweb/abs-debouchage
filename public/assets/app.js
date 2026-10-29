(function(){
  var d=document, root=d.documentElement;
  root.classList.add("js");
  var reduce=window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Menu mobile */
  var burger=d.querySelector(".burger"), nav=d.querySelector(".nav");
  if(burger&&nav){
    burger.addEventListener("click",function(){
      var hb=d.querySelector(".header").getBoundingClientRect().bottom; nav.style.setProperty("--nav-top",Math.round(hb)+"px");
      var o=nav.classList.toggle("open");
      burger.setAttribute("aria-expanded",o);
      d.body.style.overflow=o?"hidden":"";
    });
    nav.addEventListener("click",function(e){ if(e.target.closest("a")){nav.classList.remove("open");d.body.style.overflow="";burger.setAttribute("aria-expanded","false");}});
  }
  /* Menu déroulant services */
  d.querySelectorAll(".dd>button").forEach(function(b){
    b.addEventListener("click",function(){var p=b.parentNode;var o=p.classList.toggle("open");b.setAttribute("aria-expanded",o);});
  });
  d.addEventListener("click",function(e){d.querySelectorAll(".dd.open").forEach(function(x){if(!x.contains(e.target)&&window.innerWidth>959){x.classList.remove("open");}});});
  d.addEventListener("keydown",function(e){if(e.key==="Escape"){d.querySelectorAll(".dd.open").forEach(function(x){x.classList.remove("open");});}});

  /* Devis WhatsApp */
  d.querySelectorAll("form[data-wa]").forEach(function(f){
    var M=JSON.parse(f.getAttribute("data-wa"));
    f.addEventListener("submit",function(e){
      e.preventDefault();
      var p=f.querySelector("input[name=prob]:checked");
      var where=f.querySelector("[name=where]").value.trim();
      var err=f.querySelector(".err");
      if(!p||!where){err.classList.add("show"); (p?f.querySelector("[name=where]"):f.querySelector("input[name=prob]")).focus(); return;}
      err.classList.remove("show");
      var urg=f.querySelector("input[name=urg]:checked").value;
      var name=f.querySelector("[name=name]").value.trim();
      var det=f.querySelector("[name=det]").value.trim();
      var lines=[M.hello,"","🔧 "+M.prob+" : "+p.getAttribute("data-label"),"⏱ "+M.urg+" : "+M.urgv[urg],"📍 "+M.where+" : "+where];
      if(name) lines.push("👤 "+M.name+" : "+name);
      if(det) lines.push("📝 "+M.det+" : "+det);
      lines.push("","("+location.pathname+")");
      window.open("https://wa.me/"+M.num+"?text="+encodeURIComponent(lines.join("\n")),"_blank","noopener");
    });
  });

  /* Apparition au défilement */
  var els=d.querySelectorAll(".reveal");
  if(!reduce && "IntersectionObserver" in window){
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target);}});},{rootMargin:"0px 0px -8% 0px"});
    els.forEach(function(el,i){el.style.transitionDelay=(Number(el.getAttribute("data-d"))||0)*70+"ms";io.observe(el);});
  } else { els.forEach(function(el){el.classList.add("in");}); }

  /* Compte à rebours de l'illustration */
  var eta=d.querySelector("[data-eta]");
  if(eta && !reduce){
    var n=27; setInterval(function(){ n=n<=14?27:n-1; eta.textContent=n; },2600);
  }
})();
