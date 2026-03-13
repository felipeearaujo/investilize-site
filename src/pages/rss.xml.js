import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('blog');
  
  return rss({
    title: 'Investilize | Blog',
    description: 'Educação financeira e ferramentas.',
    site: context.site,
    items: posts.map((post) => {
      // Gera a URL absoluta da imagem
      const imageUrl = new URL(post.data.heroImage.src || post.data.heroImage, context.site).href;
      
      return {
        title: post.data.title,
        pubDate: post.data.pubDate,
        description: post.data.description,
        link: `/blog/${post.id}/`,
        // O segredo para o Telegram ver a imagem é o enclosure
        customData: `<enclosure url="${imageUrl}" length="0" type="image/png" />`,
      };
    }),
    customData: `<language>pt-br</language>`,
  });
}