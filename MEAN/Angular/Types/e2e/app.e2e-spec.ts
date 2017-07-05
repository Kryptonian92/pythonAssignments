import { TypesPage } from './app.po';

describe('types App', () => {
  let page: TypesPage;

  beforeEach(() => {
    page = new TypesPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
