(function(){
 const fmt=v=>v.toLocaleString('pt-BR',{style:'currency',currency:'BRL',maximumFractionDigits:0});
 const inp=document.getElementById('conta'),rng=document.getElementById('contaR');
 if(!inp)return;
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
 inp.addEventListener('input',()=>{rng.value=parseFloat(inp.value.replace(/\D/g,''))||0;calc()});
 rng.addEventListener('input',()=>{inp.value=rng.value;calc()});
 document.querySelectorAll('.seg button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('.seg button').forEach(x=>x.setAttribute('aria-pressed','false'));
  b.setAttribute('aria-pressed','true');tipo=b.dataset.t;calc();}));
 calc();
 const f=document.getElementById('orc');
 f&&f.addEventListener('submit',e=>{e.preventDefault();
  const d=new FormData(f);
  const msg=`Olá! Quero um orçamento de energia solar.\nNome: ${d.get('nome')}\nCidade: ${d.get('cidade')}\nTipo de imóvel: ${d.get('tipo')}\nValor médio da conta: R$ ${d.get('valor')}\n${d.get('obs')?'Obs.: '+d.get('obs'):''}`;
  window.open('https://wa.me/5561981214135?text='+encodeURIComponent(msg),'_blank');
  if(window.gtag)gtag('event','generate_lead');});
})();