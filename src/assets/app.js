(function(){
  var d=document, root=d.documentElement, w=window;
  root.classList.add("js");
  var reduce=w.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var header=d.querySelector(".header");
  function headerBottom(){return Math.max(0,Math.round(header.getBoundingClientRect().bottom));}

  /* ---------- Menu mobile ---------- */
  var burger=d.querySelector(".burger"), nav=d.querySelector(".nav");
  if(burger&&nav){
    burger.addEventListener("click",function(){
      nav.style.setProperty("--nav-top",headerBottom()+"px");
      var o=nav.classList.toggle("open");
      burger.setAttribute("aria-expanded",o); d.body.style.overflow=o?"hidden":"";
    });
    nav.addEventListener("click",function(e){if(e.target.closest("a")){nav.classList.remove("open");d.body.style.overflow="";burger.setAttribute("aria-expanded","false");}});
  }
  d.querySelectorAll(".dd>button").forEach(function(b){
    b.addEventListener("click",function(){var o=b.parentNode.classList.toggle("open");b.setAttribute("aria-expanded",o);});
  });
  d.addEventListener("click",function(e){d.querySelectorAll(".dd.open").forEach(function(x){if(!x.contains(e.target)&&w.innerWidth>959)x.classList.remove("open");});});
  d.addEventListener("keydown",function(e){if(e.key==="Escape")d.querySelectorAll(".dd.open").forEach(function(x){x.classList.remove("open");});});

  /* ---------- Devis WhatsApp ---------- */
  d.querySelectorAll("form[data-wa]").forEach(function(f){
    var M=JSON.parse(f.getAttribute("data-wa"));
    f.addEventListener("submit",function(e){
      e.preventDefault();
      var p=f.querySelector("input[name=prob]:checked"), where=f.querySelector("[name=where]").value.trim(), err=f.querySelector(".err");
      if(!p||!where){err.classList.add("show");(p?f.querySelector("[name=where]"):f.querySelector("input[name=prob]")).focus();return;}
      err.classList.remove("show");
      var urg=f.querySelector("input[name=urg]:checked").value, name=f.querySelector("[name=name]").value.trim(), det=f.querySelector("[name=det]").value.trim();
      var lines=[M.hello,"","🔧 "+M.prob+" : "+p.getAttribute("data-label"),"⏱ "+M.urg+" : "+M.urgv[urg],"📍 "+M.where+" : "+where];
      if(name)lines.push("👤 "+M.name+" : "+name);
      if(det)lines.push("📝 "+M.det+" : "+det);
      lines.push("","("+location.pathname+")");
      w.open("https://wa.me/"+M.num+"?text="+encodeURIComponent(lines.join("\n")),"_blank","noopener");
    });
  });

  /* ---------- Apparitions ---------- */
  var els=d.querySelectorAll(".reveal,.wipe");
  if(!reduce&&"IntersectionObserver" in w){
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target);}});},{rootMargin:"0px 0px -8% 0px"});
    els.forEach(function(el){el.style.transitionDelay=(Number(el.getAttribute("data-d"))||0)*80+"ms";io.observe(el);});
  } else els.forEach(function(el){el.classList.add("in");});

  /* ---------- Avant / après ---------- */
  d.querySelectorAll(".ba-view").forEach(function(v){
    var r=v.querySelector("input");
    function set(){v.style.setProperty("--pos",r.value+"%");}
    r.addEventListener("input",set); set();
  });

  /* ---------- Histoire du débouchage (pilotée par le défilement) ---------- */
  var story=d.querySelector(".story"), S={};
  if(story){
    S.steps=story.querySelectorAll(".story-steps li");
    S.svg=story.querySelector(".story-svg");
    S.cam=S.svg.querySelector("#cam"); S.cone=S.svg.querySelector("#cone");
    S.tool=S.svg.querySelector("#tool"); S.cable=S.svg.querySelector("#cable");
    S.clog=S.svg.querySelector("#clog"); S.back=S.svg.querySelector("#back");
    S.flow=S.svg.querySelector("#flow"); S.jet=S.svg.querySelector("#jet"); S.ok=S.svg.querySelector("#ok");
    S.lbl=story.querySelector("[data-state]"); S.dist=story.querySelector("[data-dist]");
    S.states=JSON.parse(story.getAttribute("data-states"));
  }
  function clamp(x,a,b){return Math.max(a,Math.min(b,x));}
  function seg(p,a,b){return clamp((p-a)/(b-a),0,1);}
  function drawStory(){
    var ol=story.querySelector(".story-steps"), r=ol.getBoundingClientRect(), vh=w.innerHeight;
    var first=S.steps[0].getBoundingClientRect(), last=S.steps[S.steps.length-1].getBoundingClientRect();
    var a=first.top, b=last.bottom;
    var p=clamp((vh*0.5-a)/(b-a),0,1);
    if(reduce)p=1;
    var camX=-60+seg(p,0,.18)*370;               // caméra qui avance jusqu'au bouchon
    var camOut=seg(p,.2,.27);                    // puis ressort
    var tX=-40+seg(p,.26,.44)*340;                  // furet qui avance
    var hit=seg(p,.36,.5);                        // le bouchon se casse
    var jet=seg(p,.46,.62);                        // haute pression
    var flow=seg(p,.58,.72);                       // l'eau s'écoule
    S.cam.setAttribute("transform","translate("+(camX-camOut*400)+",0)");
    S.cone.setAttribute("opacity",(1-camOut)*(p>0.02?1:0));
    S.cable.setAttribute("x2",Math.max(0,tX-10)); S.tool.setAttribute("transform","translate("+tX+",0)");
    S.tool.setAttribute("opacity",p>.24&&p<.66?1:0); S.cable.setAttribute("opacity",p>.24&&p<.66?1:0);
    var sc=1-Math.max(hit*.55,jet);
    S.clog.setAttribute("transform","translate(380 200) scale("+Math.max(sc,0.001)+") translate(-380 -200)");
    S.clog.setAttribute("opacity",sc<0.05?0:1);
    S.back.setAttribute("height",64*(1-flow)+6); S.back.setAttribute("y",246-(64*(1-flow)+6));
    S.jet.setAttribute("opacity",jet>0&&jet<1?1:0);
    S.flow.setAttribute("opacity",flow);
    S.ok.setAttribute("opacity",seg(p,.7,.8));
    var k=0,best=1e9; S.steps.forEach(function(li,i){var q=li.getBoundingClientRect();var dd=Math.abs(q.top+q.height/2-vh*0.5);if(dd<best){best=dd;k=i;}});
    S.steps.forEach(function(li,i){li.classList.toggle("on",i===k);});
    if(S.lbl)S.lbl.textContent=S.states[k];
    if(S.dist)S.dist.textContent=(Math.max(0,camX+60)/370*3.4).toFixed(2).replace(".",",")+" m";
  }

  /* ---------- Boucle de défilement ---------- */
  var par=d.querySelectorAll("[data-par]"), mp=d.querySelector(".mpipe"), ticking=false;
  function onScroll(){
    var h=root.scrollHeight-w.innerHeight, s=h>0?w.scrollY/h:0;
    root.style.setProperty("--scroll",s.toFixed(4));
    if(mp)mp.style.setProperty("--mpipe-top",headerBottom()+"px");
    if(!reduce)par.forEach(function(el){var r=el.getBoundingClientRect();var c=(r.top+r.height/2-w.innerHeight/2)/w.innerHeight;el.style.setProperty("--par",(c*-60).toFixed(1)+"px");});
    if(story)drawStory();
    if(story&&w.innerWidth<=900)story.style.setProperty("--nav-h",headerBottom()+"px");
    ticking=false;
  }
  w.addEventListener("scroll",function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll);}},{passive:true});
  w.addEventListener("resize",onScroll);
  onScroll();
})();
