// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import netlify from '@astrojs/netlify';
import partytown from '@astrojs/partytown';

// https://astro.build/config
export default defineConfig({
  site: 'https://investilize.com.br',
  
  // ✅ NOVO: Garante que o sitemap e os canonicals sempre tenham a barra final, alinhando com a Netlify
  trailingSlash: 'always',

  // ✅ CORREÇÃO FINAL: Usando a estrutura de objeto com 'entrypoint'
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp' 
    }
  },

  integrations: [mdx(), sitemap(), partytown()],

  // ✅ NOVO: Redirecionamento 301 para corrigir o erro de digitação da URL
  redirects: {
    '/blog/renda-fix-veriavel-diferenca': { status: 301, destination: '/blog/renda-fixa-variavel-diferenca/' },
    '/blog/renda-fix-veriavel-diferenca/': { status: 301, destination: '/blog/renda-fixa-variavel-diferenca/' },
  },

  adapter: netlify({
    imageCDN: false
  }),
});