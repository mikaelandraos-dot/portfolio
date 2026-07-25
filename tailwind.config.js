/** Configuration Tailwind du portfolio.
 *  Reprend la palette « Grâce Institutionnelle » qui était dupliquée
 *  dans le <head> de chacune des 11 pages.
 *
 *  `content` liste les fichiers parcourus pour ne garder que les classes
 *  réellement utilisées (l'ancien « purge »). Le JavaScript du site est écrit
 *  à l'intérieur des fichiers HTML : il est donc déjà couvert.
 *
 *  Règle à retenir : ne jamais composer un nom de classe par concaténation
 *  (`h-${n}`), sinon la classe n'est pas détectée et disparaît à la
 *  compilation. Les classes injectées en JS doivent apparaître en toutes
 *  lettres dans la source, comme "h-9 sm:h-11" dans trustedByData.
 */
module.exports = {
  content: [
    './*.html',
    './blog/*.html',
    './blog-articles/*.html',
  ],
  theme: {
    extend: {
      colors: {
        // Grâce Institutionnelle — bleu encre
        brand: { 50:'#eef1f8', 100:'#e0e6f3', 400:'#41538f', 500:'#1e3a8a', 600:'#15295f', 900:'#0f1f49' },
        indigo: { 500:'#1e3a8a' },
        // palette chaude (ivoire / anthracite) substituée à slate
        slate: { 50:'#faf7f1', 100:'#f1ead9', 200:'#e6dfce', 300:'#d3c9b2', 400:'#9b9486', 500:'#7c7567', 600:'#574f40', 700:'#3e3729', 800:'#2a2820', 900:'#1c2b3a', 950:'#141b24' }
      },
      fontFamily: {
        display: ['Gloock', 'serif'],
        sans: ['Instrument Sans', 'sans-serif'],
        mono: ['Geist Mono', 'monospace'],
      }
    }
  }
}
