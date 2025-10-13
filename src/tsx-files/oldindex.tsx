import oldindex from '../raw/oldindex.html?raw'; // vs code is complaining about this but it works fine?
import HtmlPage from './scripts/HtmlPage';

export default function htmlHelper() {
  return <HtmlPage html={oldindex} />;
}