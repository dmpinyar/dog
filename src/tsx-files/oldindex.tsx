import oldindex from '../raw/oldindex.html?raw';
import HtmlPage from './scripts/HtmlPage';

export default function htmlHelper() {
  return <HtmlPage html={oldindex} />;
}