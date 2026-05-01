// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import netlify from '@astrojs/netlify';
import partytown from '@astrojs/partytown';

// https://astro.build/config
export default defineConfig({
  site: 'https://investilize.com.br',

  // ✅ Mantém a barra final em todos os links para alinhar com a Netlify
  trailingSlash: 'always',

  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  },

  integrations: [mdx(), sitemap(), partytown()],

  // ✅ CORREÇÃO: Apenas uma rota de redirecionamento para evitar colisão
  redirects: {
    '/blog/renda-fix-veriavel-diferenca/': { status: 301, destination: '/blog/renda-fixa-variavel-diferenca/' },
  },

  adapter: netlify({
    imageCDN: false
  }),
});
