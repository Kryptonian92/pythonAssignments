import { PowerPage } from './app.po';

describe('power App', () => {
  let page: PowerPage;

  beforeEach(() => {
    page = new PowerPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
