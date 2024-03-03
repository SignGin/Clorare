import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { AUTH_LOGIN_LINK, TOKEN_ID } from './utils/constants';

export function middleware(request: NextRequest) {
  // 리다이렉트 조건
  if (!request.cookies.get(TOKEN_ID)) {
    return NextResponse.redirect(new URL(AUTH_LOGIN_LINK, request.url));
  }
}

export const config = {
  // 이 Middleware가 동작할 경로들
  matcher: '/notUse/clothes/:path*',
};
