(function(){
 const fmt=v=>v.toLocaleString('pt-BR',{style:'currency',currency:'BRL',maximumFractionDigits:0});
 const inp=document.getElementById('conta'),rng=document.getElementById('contaR');
 if(inp){ // simulador (só nas páginas que têm)
 let tipo='residencial';
 // Premissas conservadoras (estimativa): tarifa média c/ impostos ~R$ 1,00/kWh; geração média ~120 kWh/mês por kWp no DF/GO;
 // economia de 75% a 90% do valor da conta (permanecem taxa mínima, iluminação pública e encargos de rede).
 function calc(){
  let v=parseFloat(String(inp.value).replace(/\D/g,''))||0;
  const kwh=v/1.0, kwp=Math.max(kwh/120,0), placas=Math.ceil(kwp*1000/580);
  const eMin=v*.75, eMax=v*.90;
  document.getElementById('rMes').textContent=v?fmt(eMin)+' a '+fmt(eMax):'—';
  document.getElementById('rAno').textContent=v?fmt(eMin*12)+'+':'—';
  document.getElementById('r25').textContent=v?fmt(eMin*12*25)+'+':'—';
  document.getElementById('rKwp').textContent=v?kwp.toFixed(1).replace('.',',')+' kWp':'—';
  document.getElementById('rPlacas').textContent=v?('≈ '+placas+' placas'):'—';
  const msg=`Olá! Fiz a simulação no site da MS Luz Solar. Minha conta de luz é de ${fmt(v)} por mês (${tipo}). Quero uma proposta de energia solar.`;
  document.getElementById('simWa').href='https://wa.me/5561981214135?text='+encodeURIComponent(msg);
 }
 let su=false;const used=()=>{if(su)return;su=true;window.gtag&&gtag('event','simulador_uso');window.fbq&&fbq('trackCustom','SimuladorUso');};
 inp.addEventListener('input',()=>{used();rng.value=parseFloat(inp.value.replace(/\D/g,''))||0;calc()});
 rng.addEventListener('input',()=>{used();inp.value=rng.value;calc()});
 document.querySelectorAll('.seg button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('.seg button').forEach(x=>x.setAttribute('aria-pressed','false'));
  b.setAttribute('aria-pressed','true');tipo=b.dataset.t;calc();}));
 calc();
 }
 const f=document.getElementById('orc');
 const WEBHOOK='https://hook.us2.make.com/gjjw1e8e20fba1ljsn7djqrvyji3e2un';
 f&&f.addEventListener('submit',e=>{e.preventDefault();
  const st=document.getElementById('orc-st'),btn=f.querySelector('button[type=submit]');
  if(f.empresa_site.value)return;
  let tel=f.telefone.value.replace(/\D/g,'');if(tel.indexOf('55')!==0)tel='55'+tel;
  if(!f.nome.value.trim()||!f.aceite.checked||tel.length<12||tel.length>13||!f.valor.value.trim()){st.textContent='Confira nome, telefone, valor da conta e o aceite.';return;}
  const d=new FormData(f);
  const msg=`Olá! Quero uma simulação de energia solar.\nNome: ${d.get('nome')}\nCidade: ${d.get('cidade')}\nTipo de imóvel: ${d.get('tipo')}\nValor médio da conta: R$ ${d.get('valor')}${d.get('obs')?'\nObs.: '+d.get('obs'):''}`;
  const wa='https://wa.me/5561981214135?text='+encodeURIComponent(msg);
  const p=new URLSearchParams({empresa:'MS Luz Solar',nome:f.nome.value.trim(),telefone:tel,cidade:d.get('cidade'),
   tipo_servico:'Energia solar - '+d.get('tipo'),valor_conta:d.get('valor'),obs:d.get('obs')||'',origem:location.href,
   gclid:new URLSearchParams(location.search).get('gclid')||'',data_envio:new Date().toISOString()});
  btn.disabled=true;st.textContent='Enviando...';
  const c=new AbortController(),t=setTimeout(()=>c.abort(),8000);
  fetch(WEBHOOK,{method:'POST',mode:'no-cors',body:p,signal:c.signal})
   .then(()=>{if(window.gtag)gtag('event','conversion',{'send_to':'AW-11471703423/8kKYCIWuragdEP-akd4q'});if(window.gtag)gtag('event','generate_lead',{empresa:'MS Luz Solar'});window.fbq&&fbq('track','Lead',{content_name:'simulacao_energia_solar'});
     st.innerHTML='Pedido registrado! Abrindo o WhatsApp com a sua mensagem pronta — é só tocar em <b>enviar</b>. Se não abrir, <a href="'+wa+'">toque aqui</a>.';f.reset();setTimeout(()=>{location.href=wa;},900);})
   .catch(()=>{st.innerHTML='Abrindo o WhatsApp para você enviar o pedido... Se não abrir, <a href="'+wa+'">toque aqui</a>.';location.href=wa;})
   .finally(()=>{clearTimeout(t);btn.disabled=false;});});
 // máscara de telefone
 const tf=f&&f.telefone;tf&&tf.addEventListener('input',()=>{let d=tf.value.replace(/\D/g,'').slice(0,11);
  tf.value=d.length>10?`(${d.slice(0,2)}) ${d.slice(2,3)} ${d.slice(3,7)}-${d.slice(7)}`:d.length>6?`(${d.slice(0,2)}) ${d.slice(2,6)}-${d.slice(6)}`:d.length>2?`(${d.slice(0,2)}) ${d.slice(2)}`:d;});
 // eventos: início do formulário
 let fs=false;f&&f.addEventListener('focusin',()=>{if(fs)return;fs=true;window.gtag&&gtag('event','form_start',{form:'simulacao'});});
 // conversões: cliques no WhatsApp e no telefone (mesmas ações do Google Ads da MS)
 document.addEventListener('click',e=>{const a=e.target.closest&&e.target.closest('a[href]');if(!a||typeof gtag!=='function')return;
  const h=a.getAttribute('href')||'';
  if(h.indexOf('https://wa.me/')===0){gtag('event','conversion',{'send_to':'AW-11471703423/no1fCM-0yZIdEP-akd4q'});gtag('event','clique_whatsapp');window.fbq&&fbq('track','Contact',{method:'whatsapp'});}
  else if(h.indexOf('tel:')===0){gtag('event','conversion',{'send_to':'AW-11471703423/o9v9CNK0yZIdEP-akd4q'});gtag('event','clique_telefone');window.fbq&&fbq('track','Contact',{method:'telefone'});}},true);
 // aviso de cookies
 const ck=document.getElementById('ck');let seen=null;try{seen=localStorage.getItem('ck')}catch(e){}
 if(ck&&!seen){ck.style.display='flex';document.getElementById('ckok').onclick=()=>{ck.style.display='none';try{localStorage.setItem('ck','1')}catch(e){}};}
})();