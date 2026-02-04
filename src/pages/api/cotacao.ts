import type { APIRoute } from 'astro';

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();
    let symbol = body.symbol;

    if (!symbol) {
      return new Response(JSON.stringify({ error: 'Símbolo não fornecido' }), {
        status: 400,
      });
    }

    // Tratamento básico para garantir letras maiúsculas
    symbol = symbol.toUpperCase();

    // 1. Buscamos os dados no Yahoo Finance (Endpoint gratuito e público)
    // Usamos o endpoint 'chart' que retorna metadados precisos do preço atual
    const response = await fetch(
      `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}?interval=1d&range=1d`
    );

    if (!response.ok) {
      return new Response(JSON.stringify({ error: 'Ativo não encontrado ou erro na API externa' }), {
        status: 404,
      });
    }

    const data = await response.json();

    // 2. Verificamos se a resposta tem o formato esperado
    if (!data.chart || !data.chart.result || data.chart.result.length === 0) {
      return new Response(JSON.stringify({ error: 'Dados inválidos recebidos' }), {
        status: 404,
      });
    }

    // 3. Extraímos os dados importantes
    const meta = data.chart.result[0].meta;
    const price = meta.regularMarketPrice;
    const previousClose = meta.chartPreviousClose;
    
    // Calculamos a variação se a API não entregar pronta
    const change = price - previousClose;
    const changePercent = (change / previousClose) * 100;

    // 4. Montamos o JSON de resposta para o seu Frontend
    return new Response(
      JSON.stringify({
        symbol: meta.symbol,
        price: price.toFixed(2), // Preço com 2 casas
        change: change.toFixed(2), // Variação em R$
        changePercent: changePercent.toFixed(2) + '%', // Variação em %
        currency: meta.currency,
        timestamp: new Date().toISOString()
      }),
      {
        status: 200,
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );

  } catch (error) {
    console.error('Erro na API de cotação:', error);
    return new Response(JSON.stringify({ error: 'Erro interno no servidor' }), {
      status: 500,
    });
  }
};