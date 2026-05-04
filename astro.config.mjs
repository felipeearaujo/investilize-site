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

  build: {
    format: 'directory' // Isso ajuda a criar pastas físicas (index.html) para cada post
  },

  // ✅ CORREÇÃO FINAL: Usando a estrutura de objeto com 'entrypoint'
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp' 
    }
  },

  integrations: [mdx(), sitemap(), partytown()],

  adapter: netlify({
    imageCDN: false
  }),
});