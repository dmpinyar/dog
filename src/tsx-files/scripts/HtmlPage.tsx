import React from 'react';

type HtmlPageProps = { html: string };

export default function HtmlPage({ html }: HtmlPageProps) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}